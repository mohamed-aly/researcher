"""Search local Markdown sources and show traceable passages."""

from pathlib import Path
import re
import sys

SOURCES = Path(__file__).parent / "sources"


def search(query: str, limit: int = 5) -> list[dict[str, str | int]]:
    """Rank source lines by query-term overlap; return source and line citations."""
    terms = {term.lower() for term in re.findall(r"[\w'-]+", query) if len(term) > 2}
    if not terms:
        return []

    matches: list[dict[str, str | int]] = []
    for path in sorted(SOURCES.rglob("*.md")):
        for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            words = {word.lower() for word in re.findall(r"[\w'-]+", line)}
            overlap = len(terms & words)
            if overlap:
                matches.append({
                    "source": str(path.relative_to(SOURCES)),
                    "line": line_number,
                    "score": overlap,
                    "text": line.strip(),
                })

    matches.sort(key=lambda item: (-int(item["score"]), str(item["source"]), int(item["line"])))
    return matches[:limit]


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit('Usage: python3 researcher.py "your research question"')

    query = " ".join(sys.argv[1:])
    results = search(query)
    if not results:
        print("No matching passages found. Add Markdown documents under sources/ or try different terms.")
        return

    print(f"Research question: {query}\n\nMatching passages:")
    for result in results:
        print(f"- {result['text']} [{result['source']}:{result['line']}]")


if __name__ == "__main__":
    main()
