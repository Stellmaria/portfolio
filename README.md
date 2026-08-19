# Portfolio

Static personal portfolio for Anastasia Melnikova, focused on Java backend work and public GitHub projects.

## Live site

GitHub Pages: https://stellmaria.github.io/portfolio/

## Current profile focus

The site reflects technologies that are currently used across the public repositories rather than a generic skills wishlist.

### Backend

- Java 17
- Spring Boot / Spring MVC
- Spring Security
- Spring Data JPA / Hibernate
- Jakarta Servlet / JSP

### Data

- PostgreSQL / SQL
- JDBC
- QueryDSL
- Liquibase
- Flyway

### Testing and build

- JUnit 5
- Mockito
- Testcontainers
- Spring Test
- Maven
- Gradle

### Web and delivery

- Thymeleaf
- HTML / CSS / JavaScript
- Git / GitHub
- GitHub Actions
- Docker Compose

## Featured projects

- [library](https://github.com/Stellmaria/library) — Spring Boot MVC library application with role-based security, PostgreSQL, QueryDSL, Liquibase and Testcontainers;
- [airport](https://github.com/Stellmaria/airport) — Java 17 JDBC/DAO airport domain with connection pooling, PostgreSQL integrity rules and integration tests;
- [sql](https://github.com/Stellmaria/sql) — PostgreSQL course assignments with Flyway migrations and SQL verification in CI;
- [servlets](https://github.com/Stellmaria/servlets) — Jakarta Servlet/JSP session-authentication demo with JUnit 5 and Mockito;
- [java-core](https://github.com/Stellmaria/java-core) — Java 17 fundamentals exercises with automated tests and Gradle CI;
- [flower-shop](https://github.com/Stellmaria/flower-shop) — OOP and collections practice with validation, sorting, searching and JUnit tests.

## Site sections

- responsive hero with current backend focus;
- profile/about section linked to the GitHub account;
- grouped current technology stack;
- six selected public project cards with accurate descriptions and direct repository links;
- mobile-friendly layout and accessible focus states;
- image fallback for the hero;
- background video only on larger screens when reduced motion is not requested.

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
