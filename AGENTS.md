# AGENTS.md

Guide for AI coding agents working on this project.

## Money rules
- Always store money as whole cents (int), never float.
  Example: $100.00 is 10000.
- When splitting, every cent must be paid by someone.
  The shares must always add up to the exact total.
- Run `python -m pytest` after every change. All tests must pass.
