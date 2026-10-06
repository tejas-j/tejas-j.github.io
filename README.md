# tejasrj.io

Personal website of Tejas R. Jammihal, built with Jekyll and hosted on GitHub Pages.

## Editing content

- `_data/publications.yml`: publications, preprints, abstracts and talks. Add a new entry at the top of its group; set `highlight: true` to feature it on the home page and `cofirst: true` to mark co-first authorship.
- `_data/cv.yml`: experience, education, skills, honors and service shown on `/cv/`.
- `index.html`: home page text (about, research areas, selected work, side project).
- `training-log.html`: the side-project page; the architecture diagram is inline SVG, screenshots live in `assets/img/training-log/`.
- `_config.yml`: name, title, affiliation, links and the CV PDF path.
- `assets/Tejas_Jammihal_CV.pdf`: the downloadable CV. Replace the file to update it.
- `assets/img/avatar.jpg`: the home page portrait (square; the page shows it as a circle).
- `llms.txt`: plain-text summary for AI assistants; it pulls publications from the data file, so only the prose needs updating.
- When you change a page, bump its `last_modified_at` front matter so the sitemap reflects it.

## Local preview

```sh
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.
