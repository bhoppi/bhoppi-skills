#!/usr/bin/env python3
"""
HTML Cleaner Script

Removes style attributes and empty tags from HTML files.
Recursively processes until no changes remain.
"""

import re
import sys
from pathlib import Path

SELF_CLOSING_TAGS = {
    "br",
    "img",
    "input",
    "hr",
    "meta",
    "link",
    "area",
    "base",
    "col",
    "embed",
    "param",
    "source",
    "track",
    "wbr",
    "circle",
    "rect",
    "line",
    "polyline",
    "polygon",
    "ellipse",
}


def remove_style_attributes(html: str) -> str:
    """Remove all style attributes from tags."""
    pattern = r'\s+style\s*=\s*(["\'])(?:(?!\1).)*?\1'
    return re.sub(pattern, "", html)


def is_empty_tag(tag_match: str, tag_name: str) -> bool:
    """Check if a tag is empty (no attributes, no content)."""
    tag_name_lower = tag_name.lower()

    if tag_name_lower in SELF_CLOSING_TAGS:
        return False

    attributes_match = re.search(r"<(\w+)([^>]*?)>", tag_match)
    if attributes_match:
        attrs = attributes_match.group(2).strip()
        if attrs:
            return False

    content_match = re.search(r">\s*([^<]*?)\s*<", tag_match)
    if content_match and content_match.group(1).strip():
        return False

    return True


def remove_empty_tags(html: str) -> str:
    """Remove empty tags that have no attributes and no content."""
    result = html

    empty_tag_pattern = r"<(\w+)\s*>\s*</\1>"

    while True:
        new_result = re.sub(empty_tag_pattern, "", result)
        if new_result == result:
            break
        result = new_result

    return result


def clean_html(html: str) -> tuple[str, int]:
    """
    Clean HTML by removing style attributes and empty tags.
    Returns tuple of (cleaned_html, iteration_count).
    """
    current = html
    iterations = 0

    while True:
        previous = current

        current = remove_style_attributes(current)
        current = remove_empty_tags(current)

        iterations += 1

        if current == previous:
            break

        if iterations > 100:
            print(f"Warning: Reached max iterations (100). Stopping.")
            break

    return current, iterations


def main():
    if len(sys.argv) < 2:
        print("Usage: clean_html.py <html-file-path>")
        sys.exit(1)

    source_path = Path(sys.argv[1])

    if not source_path.exists():
        print(f"Error: File not found: {source_path}")
        sys.exit(1)

    if source_path.suffix.lower() not in [".html", ".htm"]:
        print(f"Error: Not an HTML file: {source_path}")
        sys.exit(1)

    html_content = source_path.read_text(encoding="utf-8")

    cleaned_content, iterations = clean_html(html_content)

    output_path = source_path.parent / f"{source_path.stem}_cleaned.html"
    output_path.write_text(cleaned_content, encoding="utf-8")

    print(f"Source: {source_path}")
    print(f"Output: {output_path}")
    print(f"Iterations: {iterations}")
    print("Done.")


if __name__ == "__main__":
    main()
