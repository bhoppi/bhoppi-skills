---
name: html-cleaner
description: Cleans HTML files by removing all style attributes from tags and removing empty tags (tags with no attributes and no content). Recursively processes until no changes remain. Use when user wants to clean HTML, remove formatting, or simplify HTML structure.
---

# HTML Cleaner

## Overview

This skill cleans HTML files by:
1. Removing all `style` attributes from any tag
2. Removing empty tags (tags with no attributes and no content)
3. Recursively executing both operations until the file stabilizes

## When to Use

Use this skill when:
- User says "clean HTML" or "remove HTML formatting"
- User wants to simplify HTML by removing inline styles
- User wants to strip empty/wrapper tags from HTML

## Steps

### Step 1: Get Source File

1. Ask user for HTML file path if not provided
2. Verify file exists and has .html or .htm extension
3. If invalid: HALT with error

### Step 2: Process HTML

Execute the cleaning script:

```
scripts/clean_html.py [source-file-path]
```

The script will:
- Remove all `style="..."` attributes
- Remove empty tags (no attributes, no content)
- Self-closing tags are preserved (br, img, input, hr, meta, link, area, base, col, embed, param, source, track, wbr)
- Loop until no changes occur

### Step 3: Save Result

The script automatically saves output as `[original-name]_cleaned.html` in the same directory.

## Output

- Source file: `/path/to/page.html`
- Output file: `/path/to/page_cleaned.html`
