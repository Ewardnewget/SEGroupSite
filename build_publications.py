import html
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE = Path('.')

SOURCES = {
    "dblp": "https://dblp.org/pid/07/314-1.xml",
    "scholar": [
        "https://scholar.google.com/citations?user=CsyrruEAAAAJ&hl=en&oi=sra&cstart=0&pagesize=100",
        "https://scholar.google.com/citations?user=4KbafEQAAAAJ&hl=en&oi=ao&cstart=0&pagesize=100",
        "https://scholar.google.com/citations?user=gkK0P_kAAAAJ&hl=en&oi=sra&cstart=0&pagesize=100",
        "https://scholar.google.com/citations?user=QotyxBEAAAAJ&hl=en&oi=sra&cstart=0&pagesize=100",
    ],
}

HEADERS = {"User-Agent": "Mozilla/5.0"}

BOOKS = [
    {
        "title": "软件工程基础与实践",
        "cover": "https://placehold.co/240x320?text=Book+Cover",
        "desc": "围绕软件工程核心方法，覆盖需求、设计、实现、测试与维护的系统化实践。",
    },
    {
        "title": "程序分析与验证导论",
        "cover": "https://placehold.co/240x320?text=Book+Cover",
        "desc": "介绍静态分析、模型检测与形式化验证方法，强调工程可落地的分析流程。",
    },
    {
        "title": "可信软件系统构建",
        "cover": "https://placehold.co/240x320?text=Book+Cover",
        "desc": "聚焦安全与可靠性，讨论从研发流程到工具链的可信系统构建策略。",
    },
]

CCF_ABBR_MAP = {}
CCF_ABBR_ITEMS = []


def slugify_filename(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or "book"


def norm_title(t):
    t = t.lower().strip()
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"[^a-z0-9\u4e00-\u9fff ]", "", t)
    return t


def norm_venue_key(t):
    t = (t or "").lower().strip()
    t = re.sub(r"\s+", " ", t)
    t = re.sub(r"[^a-z0-9 ]", "", t)
    return t


def load_ccf_abbr_map():
    global CCF_ABBR_MAP, CCF_ABBR_ITEMS

    mapping = {}
    urls = ["https://ccf.atom.im/", "https://atom.im/ccf"]
    for url in urls:
        try:
            resp = requests.get(url, headers=HEADERS, timeout=30)
            resp.raise_for_status()
            soup = BeautifulSoup(resp.text, "html.parser")
            rows = soup.select("tr")
            for row in rows:
                cols = [c.get_text(" ", strip=True) for c in row.select("td")]
                if len(cols) < 3:
                    continue
                # Expected row format: idx | abbr | full_name | level | type | area
                abbr = cols[1].strip()
                full_name = cols[2].strip()
                if not abbr or not full_name:
                    continue
                key = norm_venue_key(full_name)
                if key and len(key) > 6:
                    mapping[key] = abbr
            if mapping:
                break
        except Exception:
            continue

    CCF_ABBR_MAP = mapping
    CCF_ABBR_ITEMS = sorted(CCF_ABBR_MAP.items(), key=lambda kv: len(kv[0]), reverse=True)


def fetch_square16_books(max_items=12):
    """Scrape 教材教辅 entries from the square16 education page.
    Returns a list of dicts: {title, cover, desc}.
    """
    url = "https://square16.org/zh/education/"
    books = []
    try:
        resp = requests.get(url, headers=HEADERS, timeout=30)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        section = None
        for h2 in soup.find_all("h2"):
            if h2.get_text(" ", strip=True) == "教材教辅":
                section = h2.find_next_sibling()
                break

        if not section:
            return []

        cards = section.select("div.flex.flex-col") or section.find_all("div", recursive=False)
        for card in cards:
            title_node = card.find(["h3", "h4"])
            if not title_node:
                continue
            title = title_node.get_text(" ", strip=True)
            if not title or title in {b["title"] for b in books}:
                continue

            img = card.find("img")
            cover = "https://placehold.co/240x320?text=Book+Cover"
            if img and img.get("src"):
                src = img.get("src")
                if src.startswith("/"):
                    src = "https://square16.org" + src
                ext = Path(src.split("?")[0]).suffix or ".jpg"
                cover = f"images/{slugify_filename(title)}{ext}"

            desc_node = card.find("p")
            authors = ""
            if desc_node:
                authors = desc_node.get_text(" ", strip=True).replace("作者：", "").strip()
            desc = f"作者：{authors}" if authors else title

            books.append({"title": title, "cover": cover, "desc": desc})
            if len(books) >= max_items:
                break
    except Exception:
        return []
    return books


def venue_abbr(venue):
    if not venue:
        return "N/A"
    venue = venue.strip()

    bad_tokens = {
        "IEEE",
        "ACM",
        "SPRINGER",
        "ELSEVIER",
        "WILEY",
        "MDPI",
        "IOS",
        "PRESS",
        "PUBLISHING",
    }

    known = {
        "international conference on software engineering": "ICSE",
        "foundations of software engineering": "FSE",
        "automated software engineering": "ASE",
        "international symposium on software testing and analysis": "ISSTA",
        "international conference on program comprehension": "ICPC",
        "software maintenance and evolution": "ICSME",
        "international conference on software analysis evolution and reengineering": "SANER",
        "mining software repositories": "MSR",
        "aaai conference on artificial intelligence": "AAAI",
        "international conference on machine learning": "ICML",
        "advances in neural information processing systems": "NeurIPS",
        "usenix security symposium": "USENIX Security",
        "international conference on computer aided verification": "CAV",
        "international conference on automated planning and scheduling": "ICAPS",
        "transactions on pattern analysis and machine intelligence": "TPAMI",
        "design, automation and test in europe": "DATE",
        "real-time systems symposium": "RTSS",
        "transactions on software engineering": "TSE",
        "transactions on reliability": "TR",
        "transactions on dependable and secure computing": "TDSC",
        "acm transactions on software engineering and methodology": "TOSEM",
        "software quality journal": "SQJ",
        "journal of systems and software": "JSS",
        "software: practice and experience": "SPE",
        "information and software technology": "IST",
        "knowledge-based systems": "KBS",
        "applied soft computing": "ASC",
        "neural networks": "NN",
    }

    lower = venue.lower()

    # Prefer exact/near matches from CCF catalog names.
    v_key = norm_venue_key(venue)
    if v_key and CCF_ABBR_ITEMS:
        for full_name_key, abbr in CCF_ABBR_ITEMS:
            if full_name_key == v_key or full_name_key in v_key or v_key in full_name_key:
                return abbr

    for k, v in known.items():
        if k in lower:
            return v

    # Keep existing all-caps abbreviations when present.
    caps_tokens = re.findall(r"\b[A-Z]{2,}\b", venue)
    for token in caps_tokens:
        if token not in bad_tokens:
            return token

    return "N/A"


def fetch_dblp():
    papers = []
    failures = []
    try:
        resp = requests.get(SOURCES["dblp"], headers=HEADERS, timeout=30)
        resp.raise_for_status()
        root = ET.fromstring(resp.text)
        for item in root:
            year_node = item.find("year")
            title_node = item.find("title")
            if year_node is None or title_node is None:
                continue
            try:
                year = int(year_node.text.strip())
            except Exception:
                continue
            title = "".join(title_node.itertext()).strip()
            if not title:
                continue
            venue = ""
            bt = item.find("booktitle")
            jt = item.find("journal")
            if bt is not None and bt.text:
                venue = bt.text.strip()
            elif jt is not None and jt.text:
                venue = jt.text.strip()
            authors = ["".join(a.itertext()).strip() for a in item.findall("author")]
            papers.append(
                {
                    "title": title,
                    "year": year,
                    "venue": venue,
                    "abbr": venue_abbr(venue),
                    "authors": authors,
                    "source": "DBLP",
                }
            )
    except Exception as e:
        failures.append(f"DBLP: {e}")
    return papers, failures


def fetch_scholar(url):
    papers = []
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    rows = soup.select("tr.gsc_a_tr")
    for row in rows:
        title_a = row.select_one("a.gsc_a_at")
        year_span = row.select_one("span.gsc_a_h") or row.select_one("span.gsc_a_yi")
        # fallback plain year cell
        year_cell = row.select_one("td.gsc_a_y")
        year_txt = ""
        if year_span and year_span.get_text(strip=True):
            year_txt = year_span.get_text(strip=True)
        elif year_cell:
            year_txt = year_cell.get_text(strip=True)

        m = re.search(r"(19|20)\d{2}", year_txt)
        if not title_a or not m:
            continue

        year = int(m.group(0))
        title = title_a.get_text(" ", strip=True)

        gray = row.select("div.gs_gray")
        authors = []
        venue = ""
        if len(gray) >= 1:
            authors = [a.strip() for a in gray[0].get_text(" ", strip=True).split(",") if a.strip()]
        if len(gray) >= 2:
            venue = gray[1].get_text(" ", strip=True)

        papers.append(
            {
                "title": title,
                "year": year,
                "venue": venue,
                "abbr": venue_abbr(venue),
                "authors": authors,
                "source": "Google Scholar",
            }
        )
    return papers


def fetch_all_scholar():
    all_papers = []
    failures = []
    for url in SOURCES["scholar"]:
        try:
            all_papers.extend(fetch_scholar(url))
        except Exception as e:
            failures.append(f"Scholar {url}: {e}")
    return all_papers, failures


def dedupe(papers):
    seen = set()
    out = []
    for p in sorted(papers, key=lambda x: (x["year"], x["title"])):
        key = (norm_title(p["title"]), p["year"])
        if key in seen:
            continue
        seen.add(key)
        out.append(p)
    return out


def sort_alumni_members_json():
    path = BASE / "members.json"
    if not path.exists():
        return
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    def degree_rank(d):
        if d == "博士":
            return 0
        if d == "硕士":
            return 1
        return 2

    alumni = data.get("毕业生", [])
    alumni.sort(
        key=lambda x: (
            -int(x.get("graduation_year") or 0),
            degree_rank(x.get("degree", "")),
            x.get("name", ""),
        )
    )
    data["毕业生"] = alumni

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def build_publications_md(papers):
    g_2020 = [p for p in papers if p["year"] >= 2020]
    g_2010_2019 = [p for p in papers if 2010 <= p["year"] <= 2019]
    g_before_2010 = [p for p in papers if p["year"] < 2010]

    def group_by_year_desc(items):
        years = {}
        for p in items:
            years.setdefault(p["year"], []).append(p)
        return sorted(years.items(), key=lambda kv: kv[0], reverse=True)

    render_counter = {"idx": 0}

    def render_group(title, items, split_year=True):
        lines = [f'<details class="pub-group">', f"<summary><h3>{title}</h3></summary>"]
        if not items:
            lines.append("<p>暂无数据。</p>")
            lines.append("</details>")
            return "\n".join(lines)

        if split_year:
            for year, year_items in group_by_year_desc(items):
                lines.append('<details class="pub-year">')
                lines.append(f"<summary><h4>{year}</h4></summary>")
                lines.append("<ul>")
                year_items_sorted = sorted(year_items, key=lambda x: x["title"].lower())
                for p in year_items_sorted:
                    authors = ", ".join(p["authors"]) if p["authors"] else "Unknown"
                    title_esc = html.escape(p["title"])
                    abbr_esc = html.escape(p["abbr"])
                    authors_esc = html.escape(authors)
                    idx = render_counter["idx"]
                    render_counter["idx"] += 1
                    lines.append(
                        f'  <li class="pub-item" data-pub-idx="{idx}"><strong>[{abbr_esc}]</strong> {title_esc} - {authors_esc}</li>'
                    )
                lines.append("</ul>")
                lines.append("</details>")
        else:
            lines.append("<ul>")
            items_sorted = sorted(items, key=lambda x: (-x["year"], x["title"].lower()))
            for p in items_sorted:
                authors = ", ".join(p["authors"]) if p["authors"] else "Unknown"
                title_esc = html.escape(p["title"])
                abbr_esc = html.escape(p["abbr"])
                authors_esc = html.escape(authors)
                idx = render_counter["idx"]
                render_counter["idx"] += 1
                lines.append(
                    f'  <li class="pub-item" data-pub-idx="{idx}"><strong>[{abbr_esc}]</strong> {title_esc} - {authors_esc}</li>'
                )
            lines.append("</ul>")
        lines.append("</details>")
        return "\n".join(lines)

    parts = []
    parts.append("---")
    parts.append("title: Publications")
    parts.append("i18n_title: research.title")
    parts.append("i18n_description: research.description")
    parts.append("---")
    parts.append("")
    parts.append('<h1 data-i18n="research.title">{% include i18n-text.html key="research.title" %}</h1>')
    parts.append("<p>以下列表来自 DBLP 与 Google Scholar 聚合结果，简称参考 CCF 会议/期刊目录（ccf.atom.im）。</p>")
    parts.append('<h2 style="margin-top: 24px;">书籍</h2>')
    parts.append(
        "<style>"
        ".book-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin:16px 0 28px 0;}"
        "@media (max-width:900px){.book-grid{grid-template-columns:repeat(2,minmax(0,1fr));}}"
        "@media (max-width:560px){.book-grid{grid-template-columns:1fr;}}"
        ".book-card{border:1px solid var(--light-gray,#e6e6e6);border-radius:10px;padding:12px;background:var(--background,#fff);}"
        ".book-cover{width:100%;aspect-ratio:3/4;object-fit:cover;border-radius:8px;display:block;margin-bottom:10px;}"
        ".book-title{font-weight:700;margin-bottom:6px;}"
        ".book-desc{font-size:.95em;line-height:1.45;color:var(--text-light,#555);margin:0;}"
        "</style>"
    )
    parts.append('<div class="book-grid">')
    for b in BOOKS:
        title_esc = html.escape(b["title"])
        desc_esc = html.escape(b["desc"])
        cover_esc = html.escape(b["cover"])
        if cover_esc.startswith("images/"):
            cover_esc = "{{ '" + cover_esc + "' | relative_url }}"
        parts.append(
            '<article class="book-card">'
            f'<img class="book-cover" src="{cover_esc}" alt="{title_esc}">'
            f'<div class="book-title">{title_esc}</div>'
            f'<p class="book-desc">{desc_esc}</p>'
            "</article>"
        )
    parts.append("</div>")
    parts.append("{% include section.html dark=true %}")
    parts.append("<h2>论文列表</h2>")
    parts.append(
        "<style>"
        ".pub-group{margin:0 0 14px}"
        ".pub-group>summary,.pub-year>summary{cursor:pointer;list-style:none;display:flex;align-items:center;gap:8px}"
        ".pub-group>summary::-webkit-details-marker,.pub-year>summary::-webkit-details-marker{display:none}"
        ".pub-group>summary::before,.pub-year>summary::before{content:'▸';display:inline-block;width:1em}"
        ".pub-group[open]>summary::before,.pub-year[open]>summary::before{content:'▾'}"
        ".pub-group>summary h3,.pub-year>summary h4{margin:0}"
        ".pub-year{margin:8px 0 10px}"
        ".pub-group ul,.pub-year ul{margin-top:8px}"
        "</style>"
    )
    parts.append(render_group("2020-现在", g_2020, split_year=True))
    parts.append(render_group("2010-2019", g_2010_2019, split_year=True))
    parts.append(render_group("2010年以前", g_before_2010, split_year=False))

    with open(BASE / "publications/index.md", "w", encoding="utf-8") as f:
        f.write("\n".join(parts) + "\n")


def main():
    load_ccf_abbr_map()

    # try to populate BOOKS from square16 教材教辅 section if available
    try:
        scraped = fetch_square16_books()
        if scraped:
            global BOOKS
            BOOKS = scraped
    except Exception:
        pass

    dblp, f1 = fetch_dblp()
    scholar, f2 = fetch_all_scholar()

    papers = dedupe(dblp + scholar)
    papers.sort(key=lambda x: (x["year"], x["title"]), reverse=True)

    with open(BASE / "publications_data.json", "w", encoding="utf-8") as f:
        json.dump(papers, f, ensure_ascii=False, indent=2)

    build_publications_md(papers)
    sort_alumni_members_json()

    failures = f1 + f2
    with open(BASE / "publications_fetch_failures.txt", "w", encoding="utf-8") as f:
        if failures:
            f.write("\n".join(failures) + "\n")
        else:
            f.write("")

    print(f"papers={len(papers)}")
    print(f"failures={len(failures)}")


if __name__ == "__main__":
    main()
