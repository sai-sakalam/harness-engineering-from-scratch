# Harness Engineering From Scratch

Learn harness engineering step by step, by building one small app: **Split the Bill**.

Three friends, a $100 dinner, and a split that should be fair. Simple to understand, and surprisingly easy for code (and AI agents) to get wrong.

This repo goes with my Medium series. Each part adds one new piece of the harness: a rule, a test, a check, or a reviewer, so AI coding agents can work on this app reliably.

## Agent = Model + Harness

You usually cannot change the AI model. You can change everything around it:

- **Guides** steer the agent *before* it acts (for example, `AGENTS.md`).
- **Sensors** check the work *after* it acts (for example, tests).

## Series progress

- [x] **Part 1: What is harness engineering?** First guide (`AGENTS.md`) and first sensor (a test that every cent is paid)
- [ ] Part 2: Guides and sensors
- [ ] Part 3: AGENTS.md as a map, not a manual
- [ ] Part 4: Tests and linters that teach your agent
- [ ] Part 5: Let one AI agent review another
- [ ] Part 6: Architecture rules for agents
- [ ] Part 7: Long-running work across sessions
- [ ] Part 8: Garbage collection for AI-written code
- [ ] Part 9: The full harness, end to end

Each finished part is tagged (`part-1`, `part-2`, ...) so you can see the repo exactly as it was at that step.

## Try it

```bash
python split_bill.py
python -m pip install pytest
python -m pytest -q
```

Expected output:

```
Shares (cents): [3334, 3333, 3333]
Total paid (cents): 10000
.
1 passed
```

## What's in here

- `split_bill.py`: the app. Money is always whole cents.
- `test_split_bill.py`: the first sensor. Shares must add up to the exact total.
- `AGENTS.md`: the first guide. Rules for AI coding agents.
- `.github/workflows/tests.yml`: runs the tests on every push, so nothing broken gets in.

## Read the series

- Part 1: *link coming soon*

If this helps you, star the repo and watch it to get updates as new parts arrive.
