# LeetCode Problem Automation Agent

Given a single LeetCode problem URL, create the local scaffold with one script run, then add the correct non-solution stub based on problem type.

## Fast Path (default)

1. Run exactly:
   `python scripts/create_problem.py <leetcode-problem-url>`
2. If the command fails, stop and report the exact error text.
3. On success, inspect the fetched problem metadata/content:
   - If the problem is Database/SQL-related, create `problems/{id}_{slug}/query.sql`.
   - Otherwise, create `problems/{id}_{slug}/main.py`.

Do not browse other URLs. Use only the URL provided by the user.

---

## What `scripts/create_problem.py` already does

The script fetches problem data from LeetCode GraphQL and writes:

- `problems/{id}_{slug}/Readme.md`
- `problems/{id}_{slug}/metadata.json`
- an upserted row in `problems.csv` (no duplicate `id` + `slug` rows on reruns)

It also normalizes raw LeetCode HTML content before writing `Readme.md` so Markdown preview rendering is cleaner (for example, removing wrapper div/class noise and repeated adjacent lines).

`metadata.json` includes:

- `id`, `slug`, `difficulty`, `topics`
- `date_solved` (today, local date)
- `url` (exact input URL)
- `attempts` initialized to `1`
- spaced review dates (`1d`, `7d`, `30d`)

---

## Stub Requirements (must follow)

After scaffolding succeeds, create stubs only (no complete solution implementation):

### `main.py`

- Use canonical Python `class Solution:` method signature for the problem.
- Keep method body as placeholder only (`# TODO` and placeholder return).
- Add a `if __name__ == "__main__":` block that runs **all official sample inputs**.
- For each sample, print:
  - placeholder result
  - expected output

### `query.sql` (for Database/SQL problems only)

- Create a SQL file scaffold with a brief header comment naming the problem.
- Add a `-- TODO` placeholder query block.
- Do not provide a completed final query.

Never provide a working solution/query.

---

## SQL Detection Rule

Treat the problem as Database/SQL if any of the following is true:

- `database` appears in topic tags from fetched metadata.
- The problem statement/title explicitly indicates SQL or database schema/table tasks.

When this rule matches, generate `query.sql` and skip `main.py`.

---

## URL Handling

Accept these forms:

- `https://leetcode.com/problems/<slug>/`
- `https://leetcode.com/problems/<slug>/description/`
- with or without trailing slash

Use the exact input URL in `metadata.json` and CSV logging.

---

## Error Handling

- If script fails (invalid URL, network/API issue, GraphQL error), report the script error and stop.
- Do not create partial stubs when scaffolding fails.
- If the target `id_slug` folder already exists, refresh files in place and avoid duplicate CSV entries.

---

## Expected Agent Output

Keep output concise:

1. Whether scaffold command succeeded.
2. Which files were created/updated.
3. If failed, exact error and where it failed.
