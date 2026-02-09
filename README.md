## Overview

This repository is a personal LeetCode practice workspace. It focuses on building repeatable scaffolding for every problem so that metadata, descriptions, and Python starter files stay consistent over time.

## Workflow

1. Run `python scripts/create_problem.py <leetcode-problem-url>` to fetch the problem via the LeetCode GraphQL API.
2. The helper script writes a new folder under `problems/` containing:
   - `Readme.md` with the official description, examples, and constraints.
   - `metadata.json` with tags, difficulty, spaced-repetition review dates, and other tracking fields.
   - An updated `problems.csv` log entry so attempts stay organized.
3. After scaffolding, add a Python stub (`main.py`) that exercises the official samples. The stub lives beside the metadata and only provides placeholders so the solution can be implemented later.

### Automation Agent

Detailed guidance for the automation process (what to run and what each artifact contains) lives in `agent_new_problem.md`. That document should be used by any tooling or contributor responsible for creating new problem skeletons so the steps stay consistent.

## Repository Layout

- `problems/` – Auto-generated folders `id_slug/` for each problem.
- `scripts/create_problem.py` – Automation script that drives metadata collection and file creation.
- `summary/` – Space for generated daily summaries.
- `agent_*.md` – Agent workflow instructions for common automation tasks.

## Goals

- Maintain a single source of truth for problem data and review schedules.
- Keep Python stubs ready so solving a problem requires minimal setup.
- Encourage deliberate practice by logging every attempt and scheduling follow-up reviews.

## Problems

The table below is generated from `problems.csv`; each entry links to the auto-generated problem folder.

| id | slug | difficulty | topics | url |
| --- | --- | --- | --- | --- |
| 88 | [merge-sorted-array](problems/88_merge-sorted-array/Readme.md) | easy | array, two-pointers, sorting | https://leetcode.com/problems/merge-sorted-array/ |
| 169 | [majority-element](problems/169_majority-element/Readme.md) | easy | array, hash-table, divide-and-conquer, sorting, counting | https://leetcode.com/problems/majority-element/ |
