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

### DSA (Python) Problems

| id | slug | difficulty | topics | url |
| --- | --- | --- | --- | --- |
| 70 | [climbing-stairs](problems/70_climbing-stairs/Readme.md) | easy | math, dynamic-programming, memoization | https://leetcode.com/problems/climbing-stairs/ |
| 88 | [merge-sorted-array](problems/88_merge-sorted-array/Readme.md) | easy | array, two-pointers, sorting | https://leetcode.com/problems/merge-sorted-array/ |
| 125 | [valid-palindrome](problems/125_valid-palindrome/Readme.md) | easy | two-pointers, string | https://leetcode.com/problems/valid-palindrome |
| 169 | [majority-element](problems/169_majority-element/Readme.md) | easy | array, hash-table, divide-and-conquer, sorting, counting | https://leetcode.com/problems/majority-element/ |
| 290 | [word-pattern](problems/290_word-pattern/Readme.md) | easy | hash-table, string | https://leetcode.com/problems/word-pattern/ |
| 383 | [ransom-note](problems/383_ransom-note/Readme.md) | easy | hash-table, string, counting | https://leetcode.com/problems/ransom-note/ |
| 392 | [is-subsequence](problems/392_is-subsequence/Readme.md) | easy | two-pointers, string, dynamic-programming | https://leetcode.com/problems/is-subsequence |

### SQL Problems

| id | slug | difficulty | topics | url |
| --- | --- | --- | --- | --- |
| 262 | [trips-and-users](problems/262_trips-and-users/Readme.md) | hard | database | https://leetcode.com/problems/trips-and-users/ |
| 1050 | [actors-and-directors-who-cooperated-at-least-three-times](problems/1050_actors-and-directors-who-cooperated-at-least-three-times/Readme.md) | easy | database | https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/ |
| 1179 | [reformat-department-table](problems/1179_reformat-department-table/Readme.md) | easy | database | https://leetcode.com/problems/reformat-department-table/ |
| 1407 | [top-travellers](problems/1407_top-travellers/Readme.md) | easy | database | https://leetcode.com/problems/top-travellers/ |
| 1587 | [bank-account-summary-ii](problems/1587_bank-account-summary-ii/Readme.md) | easy | database | https://leetcode.com/problems/bank-account-summary-ii |
| 1693 | [daily-leads-and-partners](problems/1693_daily-leads-and-partners/Readme.md) | easy | database | https://leetcode.com/problems/daily-leads-and-partners |
| 3421 | [find-students-who-improved](problems/3421_find-students-who-improved/Readme.md) | medium | database | https://leetcode.com/problems/find-students-who-improved/ |
| 3497 | [analyze-subscription-conversion](problems/3497_analyze-subscription-conversion/Readme.md) | medium | database | https://leetcode.com/problems/analyze-subscription-conversion/ |
| 3554 | [find-category-recommendation-pairs](problems/3554_find-category-recommendation-pairs/Readme.md) | hard | database | https://leetcode.com/problems/find-category-recommendation-pairs/ |
