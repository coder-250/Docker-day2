# Docker Day 2 — Dockerfiles, Custom Images & Containerization

Welcome to Day 2! You will build a Docker image for a small Python web application and run it as a container.

## Learning objectives
- Understand Dockerfile instructions.
- Build and tag a custom image.
- Run a container and map ports.
- Configure an app with environment variables.
- Inspect logs and rebuild after changing code.

## Prerequisites
Complete Day 1 and make sure Docker is running:
```bash
docker --version
docker info
```

## Repository map
```text
docker-day2-dockerfiles/
├── README.md
├── 01-dockerfile-basics/README.md
├── 02-python-web-app/
│   ├── app.py
│   ├── Dockerfile
│   ├── .dockerignore
│   └── README.md
├── 03-build-and-run/README.md
├── 04-practice-challenges/README.md
└── .gitignore
```

## Quick start
Open a terminal in `02-python-web-app/`:
```bash
docker build -t day2-python-app .
docker run --name day2-python-demo -d -p 8000:8000 day2-python-app
```
Open http://localhost:8000.

Check logs and clean up:
```bash
docker logs day2-python-demo
docker rm -f day2-python-demo
```

## Troubleshooting
- Port in use: use `-p 8001:8000` and visit http://localhost:8001.
- Container name exists: run `docker rm -f day2-python-demo` first.
- Build fails: run `docker build` from inside `02-python-web-app/`.

Day 3 introduces Docker Compose and multi-container applications.
