# Portfolio

Static personal portfolio for Anastasia Melnikova, focused on Java backend learning projects and public GitHub work.

## What is included

- responsive hero, skills and project sections;
- selected public Java repositories with direct GitHub links;
- mobile-friendly layout;
- accessible navigation and focus states;
- a lightweight image fallback for the hero;
- background video only on larger screens when reduced motion is not requested;
- automated checks for broken local asset references and placeholder `href="#"` links.

## Featured projects

- [servlets](https://github.com/Stellmaria/servlets) — Jakarta Servlet/JSP session authentication demo with tests;
- [library](https://github.com/Stellmaria/library) — Spring Boot library system using persistence and security tooling;
- [airport](https://github.com/Stellmaria/airport) — Java web project with Servlets, Hibernate and PostgreSQL;
- [course-java-core](https://github.com/Stellmaria/course-java-core) — Java Core course practice across language fundamentals and standard APIs.

## Run locally

No build step or npm dependencies are required. Serve the repository root with any static HTTP server, for example:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

Opening `index.html` directly also works for most content, but an HTTP server more closely matches normal deployment behavior.

## Static checks

Run:

```bash
python scripts/check_static.py
```

The check verifies that local `src`/`href` assets referenced from `index.html` exist and rejects placeholder `href="#"` links.

GitHub Actions runs the same check on pushes and pull requests.

## Project structure

```text
.
├── css/
├── img/
├── js/
├── libs/
├── scripts/
├── video/
└── index.html
```

## Notes

The repository contains an MP4 hero background. To avoid forcing a large video download on every visitor, JavaScript skips video initialization on small screens and for visitors who enable `prefers-reduced-motion`; the existing cover image is used as the fallback.
