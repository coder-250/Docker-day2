# 01 — Dockerfile basics

A Dockerfile is a text file containing instructions Docker uses to build an image.

| Instruction | Purpose |
|---|---|
| `FROM` | Selects a base image |
| `WORKDIR` | Sets the working directory inside the image |
| `COPY` | Copies files from the build context into the image |
| `RUN` | Runs a command during image building |
| `ENV` | Sets a default environment variable |
| `EXPOSE` | Documents the port the app listens on |
| `CMD` | Sets the default command when a container starts |

## Build workflow
```text
Application files + Dockerfile -> docker build -> Image -> docker run -> Container
```

## Example
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY app.py .
ENV PORT=8000
EXPOSE 8000
CMD ["python", "app.py"]
```

Remember: `EXPOSE` does not publish a host port by itself. Use `-p 8000:8000` when running the container. The `.` in `docker build -t sample .` means the current directory is the build context.

## Quick questions
1. What is the difference between `RUN` and `CMD`?
2. When does `COPY` run?
3. Does `EXPOSE` make the app accessible from your laptop automatically?
