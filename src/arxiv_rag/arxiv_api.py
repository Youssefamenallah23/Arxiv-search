from __future__ import annotations

from collections.abc import Iterator
from datetime import UTC, datetime
import time
from urllib.parse import urlencode
from urllib.request import urlopen
import xml.etree.ElementTree as ET


ARXIV_API_URL = "https://export.arxiv.org/api/query"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}


def fetch_arxiv_page(
    query: str,
    start: int,
    max_results: int,
    sort_by: str = "submittedDate",
    sort_order: str = "descending",
    timeout_seconds: int = 30,
) -> list[dict[str, object]]:
    params = urlencode(
        {
            "search_query": query,
            "start": start,
            "max_results": max_results,
            "sortBy": sort_by,
            "sortOrder": sort_order,
        }
    )
    with urlopen(f"{ARXIV_API_URL}?{params}", timeout=timeout_seconds) as response:
        xml_bytes = response.read()

    root = ET.fromstring(xml_bytes)
    papers: list[dict[str, object]] = []
    for entry in root.findall("atom:entry", ATOM_NS):
        paper_id = _required_text(entry, "atom:id").rsplit("/", 1)[-1]
        papers.append(
            {
                "paper_id": paper_id,
                "arxiv_url": _required_text(entry, "atom:id"),
                "title": _clean_text(_required_text(entry, "atom:title")),
                "abstract": _clean_text(_required_text(entry, "atom:summary")),
                "categories": [
                    category.attrib["term"]
                    for category in entry.findall("atom:category", ATOM_NS)
                    if "term" in category.attrib
                ],
                "authors": [
                    _required_text(author, "atom:name")
                    for author in entry.findall("atom:author", ATOM_NS)
                ],
                "published": _required_text(entry, "atom:published"),
                "updated": _optional_text(entry, "atom:updated"),
                "snapshot_downloaded_at": datetime.now(UTC).isoformat(),
            }
        )
    return papers


def iter_arxiv_papers(
    query: str,
    max_results: int,
    page_size: int = 100,
    sleep_seconds: float = 3.0,
) -> Iterator[dict[str, object]]:
    seen: set[str] = set()
    fetched = 0
    while fetched < max_results:
        current_page_size = min(page_size, max_results - fetched)
        page = fetch_arxiv_page(query=query, start=fetched, max_results=current_page_size)
        if not page:
            break
        for paper in page:
            paper_id = str(paper["paper_id"])
            if paper_id in seen:
                continue
            seen.add(paper_id)
            yield paper
        fetched += len(page)
        if fetched < max_results:
            time.sleep(sleep_seconds)


def _clean_text(value: str) -> str:
    return " ".join(value.split())


def _required_text(element: ET.Element, path: str) -> str:
    child = element.find(path, ATOM_NS)
    if child is None or child.text is None:
        raise ValueError(f"Missing required arXiv field: {path}")
    return child.text


def _optional_text(element: ET.Element, path: str) -> str | None:
    child = element.find(path, ATOM_NS)
    if child is None:
        return None
    return child.text
