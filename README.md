# Task Tracker - End-to-End DevOps Mini Project

A small Flask web app delivered through a Scrum-managed CI/CD pipeline.

**Flow:** Jira (Scrum) -> GitHub -> GitHub Actions -> Docker -> Verify

## Run locally
    python -m venv .venv && source .venv/bin/activate     # Windows: .venv\Scripts\activate
    pip install -r requirements-dev.txt
    pytest --cov=app          # run tests
    flake8 .                  # lint
    python wsgi.py            # open http://localhost:5000

## Run with Docker
    docker build -t devops-mini-project .
    docker run -d -p 5000:5000 --name app devops-mini-project
    curl http://localhost:5000/health
    # or: docker compose up --build

## API
| Method | Path | Purpose |
|--------|------|---------|
| GET | /health | Health check |
| GET | /api/tasks | List tasks |
| POST | /api/tasks | Add task `{"title": "..."}` |
| PATCH | /api/tasks/<id> | Toggle done |
| DELETE | /api/tasks/<id> | Delete task |

## Pipeline (`.github/workflows/ci.yml`)
1. **build-and-test** - install deps, flake8, pytest + coverage
2. **docker** - build image, run container, smoke test `/health`
3. **publish** - push image to GitHub Container Registry (main branch only)

See `scrum/SCRUM_PLAN.md` for sprints and `docs/SCREENSHOT_CHECKLIST.md` for report screenshots.
