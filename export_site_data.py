#!/usr/bin/env python3
"""Export all site content into a single JSON file."""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

BASE = Path(__file__).resolve().parent
OUTPUT = BASE / "site_data.json"


def load_yaml(path: Path):
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path: Path):
    if not path.exists():
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def split_front_matter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    meta = yaml.safe_load(parts[1]) or {}
    body = parts[2].lstrip("\n")
    return meta, body


def read_page(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    front_matter, body = split_front_matter(text)
    return {"path": str(path.relative_to(BASE)), "front_matter": front_matter, "body": body}


def parse_home_research_cards(body: str) -> list[dict]:
    pattern = re.compile(
        r'include card\.html image="([^"]+)" title="([^"]+)" description="([^"]+)"',
    )
    return [
        {"image": m.group(1), "title": m.group(2), "description": m.group(3)}
        for m in pattern.finditer(body)
    ]


def parse_home_news(body: str) -> list[dict]:
    soup = BeautifulSoup(body, "html.parser")
    items = []
    for li in soup.select("ul li"):
        text = li.get_text(" ", strip=True)
        m = re.match(r"^(\d{4}\.\d{1,2}):\s*(.+)$", text)
        if m:
            items.append({"date": m.group(1), "text": m.group(2)})
    return items


def parse_news_page(body: str) -> list[dict]:
    soup = BeautifulSoup(body, "html.parser")
    items = []
    current_year = None
    for el in soup.find_all(["h2", "li"]):
        if el.name == "h2" and "news-year" in (el.get("class") or []):
            current_year = el.get_text(strip=True)
            continue
        if el.name != "li" or "news-item" not in (el.get("class") or []):
            continue
        tag = el.select_one(".news-tag")
        date = el.select_one(".news-date")
        title = el.select_one(".news-title")
        summary = el.select_one(".news-summary")
        items.append(
            {
                "year": current_year,
                "tag": tag.get_text(strip=True) if tag else "",
                "date": date.get_text(strip=True) if date else "",
                "title": title.get_text(strip=True) if title else "",
                "summary": summary.get_text(" ", strip=True) if summary else "",
            }
        )
    return items


def parse_books(body: str) -> list[dict]:
    soup = BeautifulSoup(body, "html.parser")
    books = []
    for card in soup.select(".book-card"):
        img = card.select_one(".book-cover")
        title = card.select_one(".book-title")
        desc = card.select_one(".book-desc")
        books.append(
            {
                "cover": img.get("src", "") if img else "",
                "title": title.get_text(strip=True) if title else "",
                "description": desc.get_text(strip=True) if desc else "",
            }
        )
    return books


def parse_publications_page(body: str) -> list[dict]:
    soup = BeautifulSoup(body, "html.parser")
    pubs = []
    current_group = None
    current_year = None
    for el in soup.find_all(["details", "li"]):
        if el.name == "details":
            summary = el.select_one("summary h3, summary h4")
            if not summary:
                continue
            label = summary.get_text(strip=True)
            classes = el.get("class") or []
            if "pub-group" in classes:
                current_group = label
                current_year = None
            elif "pub-year" in classes:
                current_year = label
            continue
        if el.name != "li" or "pub-item" not in (el.get("class") or []):
            continue
        strong = el.find("strong")
        abbr = strong.get_text(strip=True).strip("[]") if strong else ""
        rest = el.get_text(" ", strip=True)
        if strong:
            rest = rest.replace(strong.get_text(strip=True), "", 1).strip()
        title, _, authors = rest.partition(" - ")
        pubs.append(
            {
                "index": int(el.get("data-pub-idx", -1)),
                "group": current_group,
                "year": current_year,
                "abbr": abbr,
                "title": title.strip(),
                "authors": authors.strip(),
            }
        )
    return pubs


def parse_tools(body: str) -> list[dict]:
    soup = BeautifulSoup(body, "html.parser")
    tools = []
    current_tab = None
    for tab in soup.select(".tab-content"):
        current_tab = tab.get("id", "")
        for card in tab.select(".tool-card"):
            img = card.select_one(".tool-img")
            title = card.select_one("h3")
            desc = card.select_one(".tool-info p")
            links = []
            for a in card.select("a.button"):
                links.append({"text": a.get_text(" ", strip=True), "href": a.get("href", "")})
            tools.append(
                {
                    "tab_id": current_tab,
                    "image": img.get("src", "") if img else "",
                    "title": title.get_text(strip=True) if title else "",
                    "description": desc.get_text(strip=True) if desc else "",
                    "links": links,
                }
            )
    return tools


def parse_contact(body: str) -> dict:
    soup = BeautifulSoup(body, "html.parser")
    address_p = None
    for p in soup.find_all("p"):
        if p.find("i", class_=lambda c: c and "map-location" in " ".join(c)):
            address_p = p
            break
    email_link = soup.select_one('a[href^="mailto:"]')
    return {
        "address": address_p.get_text(" ", strip=True) if address_p else "",
        "email": email_link.get("href", "").replace("mailto:", "") if email_link else "",
    }


def load_collection(folder: str) -> list[dict]:
    root = BASE / folder
    if not root.exists():
        return []
    items = []
    for path in sorted(root.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        front_matter, body = split_front_matter(text)
        items.append(
            {
                "slug": path.stem,
                "path": str(path.relative_to(BASE)),
                **front_matter,
                "content": body.strip(),
            }
        )
    return items


def load_data_dir() -> dict:
    data_dir = BASE / "_data"
    result = {}
    for path in sorted(data_dir.glob("*.yaml")):
        result[path.stem] = load_yaml(path)
    return result


def main():
    config = load_yaml(BASE / "_config.yaml") or {}
    data_files = load_data_dir()

    index = read_page(BASE / "index.md")
    team = read_page(BASE / "team/index.md")
    news = read_page(BASE / "news/index.md")
    publications = read_page(BASE / "publications/index.md")
    contact = read_page(BASE / "contact/index.md")
    tools = read_page(BASE / "tools/index.md")

    export = {
        "meta": {
            "exported_at": datetime.now(timezone.utc).isoformat(),
            "repository": BASE.name,
        },
        "site": {
            "title": config.get("title"),
            "subtitle": config.get("subtitle"),
            "description": config.get("description"),
            "header": config.get("header"),
            "footer": config.get("footer"),
            "links": config.get("links", {}),
        },
        "i18n": data_files.get("i18n"),
        "members": load_json(BASE / "members.json"),
        "publications": load_json(BASE / "publications_data.json"),
        "pages": {
            "home": {
                "front_matter": index["front_matter"],
                "research_areas": parse_home_research_cards(index["body"]),
                "news_highlights": parse_home_news(index["body"]),
            },
            "team": {"front_matter": team["front_matter"]},
            "news": {
                "front_matter": news["front_matter"],
                "items": parse_news_page(news["body"]),
            },
            "publications": {
                "front_matter": publications["front_matter"],
                "books": parse_books(publications["body"]),
                "listed_papers": parse_publications_page(publications["body"]),
            },
            "contact": {
                "front_matter": contact["front_matter"],
                **parse_contact(contact["body"]),
            },
            "tools": {
                "front_matter": tools["front_matter"],
                "items": parse_tools(tools["body"]),
            },
        },
        "data": {
            k: v
            for k, v in data_files.items()
            if k != "i18n"
        },
        "posts": load_collection("_posts"),
        "members_collection": load_collection("_members"),
    }

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(export, f, ensure_ascii=False, indent=2)

    print(f"Wrote {OUTPUT}")
    print(f"  publications: {len(export['publications'] or [])}")
    print(f"  members categories: {len(export['members'] or {})}")
    print(f"  news items: {len(export['pages']['news']['items'])}")
    print(f"  listed papers (page): {len(export['pages']['publications']['listed_papers'])}")


if __name__ == "__main__":
    main()
