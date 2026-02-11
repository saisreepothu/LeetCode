# Daily Summary Automation Agent

You are an automation agent that compiles a daily summary of solved LeetCode problems based on `problems.csv` for a Python-only workflow. Run from the repository root only; no external network calls are needed.

---

## Inputs

- Optional date argument (`YYYY-MM-DD`). If omitted, default to the current local date (use this for a “today” summary).
- Source data: `problems.csv` (authoritative) and the per-problem `Readme.md` files for hyperlinks.

## Steps

1. Determine the target date:
   - Use the provided argument, or fall back to `$(date +%F)` so the default run summarizes problems solved today.
2. Generate the summary with the helper snippet (run from repo root):
   ```bash
   DATE="${1:-$(date +%F)}"
   python - <<'PY' "$DATE"
   import csv, datetime, sys, pathlib

   date = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
   rows = []
   with open('problems.csv', newline='') as f:
       for row in csv.DictReader(f):
           if row['date_solved'] == date:
               rows.append(row)

   rows.sort(key=lambda r: int(r['id']))
   sql_rows = []
   dsa_rows = []
   for r in rows:
       topics = {t.strip().lower() for t in r['topics'].split(';') if t.strip()}
       if 'database' in topics:
           sql_rows.append(r)
       else:
           dsa_rows.append(r)

   base = pathlib.Path('summary/daily')
   base.mkdir(parents=True, exist_ok=True)
   out_path = base / f'{date}.md'

   lines = [f'# Daily Summary - {date}', '']
   if not rows:
       lines.append(f'No problems solved on {date}.')
   else:
       lines.append(f'Total solved: {len(rows)}')
       counts = {}
       for r in rows:
           counts[r["difficulty"]] = counts.get(r["difficulty"], 0) + 1
       lines.append('Counts by difficulty: ' + ', '.join(f'{k}={v}' for k, v in sorted(counts.items())))
       lines.append(f'DSA (Python): {len(dsa_rows)}')
       lines.append(f'SQL: {len(sql_rows)}')
       lines.append('')
       def append_section(title, section_rows):
           lines.append(f'## {title}')
           lines.append('')
           if not section_rows:
               lines.append('No problems in this section.')
               lines.append('')
               return
           lines.append('| id | slug | difficulty | topics | url |')
           lines.append('| --- | --- | --- | --- | --- |')
           for r in section_rows:
               pid = int(r['id'])
               slug = r['slug']
               diff = r['difficulty']
               topics = r['topics'].replace(';', ', ')
               url = r['url']
               # summary files live in summary/daily/, so links must go up two levels.
               link = f'[{slug}](../../problems/{pid}_{slug}/Readme.md)'
               lines.append(f'| {pid} | {link} | {diff} | {topics} | {url} |')
           lines.append('')

       append_section('DSA (Python) Problems', dsa_rows)
       append_section('SQL Problems', sql_rows)

   out_path.write_text('\\n'.join(lines) + '\\n', encoding='utf-8')
   print(f'Wrote {out_path}')
   PY
   ```
3. Output file location: `summary/daily/<date>.md`. If no problems were solved on the target date, still emit a file noting that status.
4. Review the generated file for correctness (counts, links, difficulty, topics, URLs) before finishing.
   - Ensure problems are split into `## DSA (Python) Problems` and `## SQL Problems`.
   - Classification rule: if `database` appears in `topics`, it is SQL; otherwise DSA (Python).
5. Link safety check (must pass):
   - Because output lives in `summary/daily/`, all problem links must start with `../../problems/`.
   - Optional quick check:
     `rg -n "\]\(problems/" summary/daily/<date>.md`
   - If that command finds matches, links are wrong; regenerate/fix before finishing.

## Notes

- `problems.csv` is the single source of truth; do not hand-edit it during summary generation.
- This repository tracks Python problem work; do not mention C++ or Rust in the summary.
- Keep all formatting in Markdown; avoid adding solution code or extra commentary in the summary.
- Do not use `problems/...` as a link prefix in daily summaries; always use `../../problems/...`.
