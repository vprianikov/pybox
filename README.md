# Pybox

Monorepo workspace for Python experiments, shared package tooling, and example notebooks.

## Structure

- `packages/space` - shared package with common tooling dependencies.
- `workspaces/example` - example workspace for trying ideas and notebooks.

## Requirements

Only `uv` is required locally. The needed Python version is installed automatically.

## Quick Start

```bash
uv sync --all-packages && uv run pre-commit install --install-hooks
```

## Useful Commands

Sync only one package environment:

```bash
uv sync --package example
```

Run all pre-commit hooks:

```bash
uv run pre-commit run --all-files
```

Add dependency from repository root:

```bash
uv add requests --package example
```
