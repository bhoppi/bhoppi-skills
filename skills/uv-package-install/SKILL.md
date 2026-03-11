---
name: uv-package-install
description: Use when Python dependencies need to be installed - ensures uv is used instead of pip
---

## Trigger

**ALWAYS invoke this skill** before installing any Python dependencies. This applies to:
- Any `pip install` or `pip3 install` command
- Any Python script that requires missing packages
- Any task that mentions installing Python packages

## Installation Methods

### 1. Check uv availability first
```bash
which uv
```

If uv is not found, report error: **uv is required but not installed**. Do NOT fallback to pip.

### 2. Install single package
```bash
uv tool install <package>
```

### 3. Install with extras
```bash
uv tool install "package[extra]"
```

Examples:
- `uv tool install "requests[security]"`
- `uv tool install "pypdf[crypto]"`

### 4. Install multiple packages
```bash
uv tool install pandas numpy --with matplotlib
```

### 5. Install from requirements.txt
```bash
uv tool install --with-requirements requirements.txt
```

### 6. Run script with dependencies (preferred for one-off scripts)
```bash
uv run --with <package> python script.py
```

Examples:
- `uv run --with pandas --with openpyxl python process_excel.py`
- `uv run --with "requests>=2.28" python fetch_data.py`

### 7. Install specific version
```bash
uv tool install "pandas>=2.0,<3.0"
```

## Key Principles

- **NEVER** use `pip`, `pip3`, or `python -m pip`
- Use `uv tool install` for persistent tools that will be reused
- Use `uv run --with <package>` for temporary/script dependencies
- Support both simple package names and versioned requirements (e.g., `pandas>=2.0`)
- If uv is not found, report error and stop - do NOT attempt pip fallback
