# Contributing to POEM

Thank you for your interest in contributing to POEM! This document explains how to get involved.

## Contributor License Agreement (CLA)

**Before your first contribution can be merged, you must sign our [CLA](CLA.md).**

POEM uses dual licensing (AGPL + Commercial), so we need contributors to grant us permission to include their work in both versions. You retain all rights to your contributions.

When you open your first pull request, CLA Assistant will prompt you to sign electronically. It's quick and only needs to be done once.

## How to Contribute

### Reporting Bugs

1. Check existing issues to avoid duplicates
2. Open a new issue with a clear title and description
3. Include steps to reproduce, expected behavior, and actual behavior
4. Include your environment details (OS, Python version, Docker version)

### Suggesting Features

1. Open an issue with the `feature-request` label
2. Describe the use case and why it would benefit POEM users
3. If proposing a new integration, describe the target tool and API

### Submitting Code

1. Fork the repository
2. Create a feature branch from `main` (`git checkout -b feature/your-feature`)
3. Make your changes following our coding standards (below)
4. Add or update tests as needed
5. Ensure all tests pass
6. Commit with clear, descriptive messages
7. Push to your fork and open a pull request

### Coding Standards

- **Python:** Follow PEP 8. We use `ruff` for linting and `black` for formatting.
- **All source files** must include the AGPL copyright header (see template in repo root)
- **Prompts** go in `/prompts/defaults/` as `.txt` or `.yaml` files, not inline in code
- **Configuration** must be externalized — no hardcoded API keys, URLs, or credentials
- **Tests** are expected for new functionality

### Commit Messages

Use clear, descriptive commit messages:
- `feat: add Jira integration for Engineering Agent`
- `fix: correct context graph retrieval for cross-stage queries`
- `docs: update README with Docker setup instructions`

## Code of Conduct

All contributors are expected to follow our [Code of Conduct](CODE_OF_CONDUCT.md).

## Questions?

Open an issue or contact poem.pdm@gmail.com.
