# Scrum Plan - Task Tracker DevOps Mini Project

## Roles
| Role | Person |
|------|--------|
| Product Owner | (your name / teammate) |
| Scrum Master | (your name / teammate) |
| Development Team | (your name) |

## Product Goal
Deliver a small containerised web app (Task Tracker) through a fully automated
CI/CD pipeline: **Jira -> GitHub -> GitHub Actions -> Docker -> Verify**.

## Sprint cadence
2 sprints x 1 week each (adjust to your lab schedule).

## Sprint 1 - "Build the app" (Goal: working application in GitHub)
| Key | Story | Points |
|-----|-------|--------|
| DEV-2 | Create GitHub repository and project structure | 2 |
| DEV-3 | Implement add/list task API | 3 |
| DEV-4 | Implement complete/delete task API | 3 |
| DEV-5 | Build web UI | 3 |

## Sprint 2 - "Automate and ship" (Goal: pipeline green + container running)
| Key | Story | Points |
|-----|-------|--------|
| DEV-6 | Write unit tests with pytest | 3 |
| DEV-7 | Create GitHub Actions CI workflow | 3 |
| DEV-8 | Create Dockerfile and build image | 2 |
| DEV-9 | Add Docker build + smoke test to pipeline | 3 |
| DEV-10 | Publish image to GHCR | 2 |
| DEV-11 | Deploy and verify application in browser | 2 |
| DEV-12 | Bug: empty task title accepted | 1 |

(Your real keys will differ; DEV-1 is usually the Epic. Update this table after import.)

## Definition of Done
- Code merged to `main` via pull request
- Lint + unit tests pass in GitHub Actions
- Docker image builds and passes smoke test
- Jira issue moved to **Done**

## Scrum events (what to do + screenshot)
| Event | What to do |
|-------|-----------|
| Sprint Planning | Move stories from Backlog into the Sprint, set story points |
| Daily Scrum | Move cards To Do -> In Progress -> Done as you work |
| Sprint Review | Demo the app in the browser |
| Retrospective | Write 3 bullets: went well / to improve / action |

## Git workflow linked to Jira
Create one branch per Jira issue, put the key in branch name and commit message so Jira links them:

    git checkout -b feature/DEV-3-task-api
    git commit -m "DEV-3 add task API"
    git push -u origin feature/DEV-3-task-api   # then open a Pull Request to main
