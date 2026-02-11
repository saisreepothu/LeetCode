# README Problem Table Update Agent

Use this document whenever the Problems table in `README.md` needs to be regenerated.

## Inputs

- `problems.csv` – authoritative list of problems with IDs, slugs, difficulty level, topics, and canonical URLs.

## Steps

1. From the repository root, run the helper snippet to build two Markdown tables sorted by numeric ID:
   - `DSA (Python) Problems`
   - `SQL Problems`
   Classification rule: if `database` appears in `topics`, treat it as SQL; otherwise DSA (Python). The slug column should render as a hyperlink to each problem’s `Readme.md`.

   ```bash
   python - <<'PY'
   import csv

   dsa_rows = []
   sql_rows = []
   with open('problems.csv', newline='') as f:
       for row in csv.DictReader(f):
           entry = (
               int(row['id']),
               row['slug'],
               row['difficulty'],
               row['topics'].replace(';', ', '),
               row['url'],
           )
           topics = {t.strip().lower() for t in row['topics'].split(';') if t.strip()}
           if 'database' in topics:
               sql_rows.append(entry)
           else:
               dsa_rows.append(entry)

   dsa_rows.sort()
   sql_rows.sort()

   def print_section(title, rows):
       print(f'### {title}')
       print('')
       if not rows:
           print('No problems yet.')
           print('')
           return
       print('| id | slug | difficulty | topics | url |')
       print('| --- | --- | --- | --- | --- |')
       for pid, slug, difficulty, topics, url in rows:
           link = f'[{slug}](problems/{pid}_{slug}/Readme.md)'
           print(f'| {pid} | {link} | {difficulty} | {topics} | {url} |')
       print('')

   print_section('DSA (Python) Problems', dsa_rows)
   print_section('SQL Problems', sql_rows)
   PY
   ```

2. Copy the resulting output into the `## Problems` section in `README.md`, replacing the previous content under that heading.
3. Ensure the short lead-in sentence under `## Problems` still states that the table is generated from `problems.csv`.
4. Ensure both `### DSA (Python) Problems` and `### SQL Problems` headings exist under `## Problems`.
5. Save the file and review the diff to confirm every row includes the correct hyperlink, difficulty, topics, and URL values pulled from `problems.csv`.

The README section is now synchronized with `problems.csv`.
