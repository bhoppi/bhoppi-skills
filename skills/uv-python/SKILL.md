---
name: uv-python
description: Use uv for all Python package and script execution. Run scripts with `uv run --with`, install CLI tools with `uv tool install`, never use `--system` flag.
---

## Core Rules

For any Python-related task, you MUST follow these rules:

### 1. Running Scripts with Dependencies
When generating or running scripts, use `--with` to include dependencies:
```bash
uv run --with <package1> --with <package2> script.py
```

### 2. Installing CLI Tools
When installing CLI tools, use `uv tool install`:
```bash
uv tool install <package>
```

### 3. Script Reports Missing Dependency
When a command or script fails due to a missing dependency, rewrite it to use `uv run --with`:
```bash
uv run --with <missing-package> script.py
```

### 4. Installing CLI Tools via pip
When existing commands or scripts try to install CLI tools via pip, rewrite to use `uv tool install`:
```bash
uv tool install <package>
```

### 5. Never Use `--system`
Never add the `--system` flag to `uv pip` commands.
