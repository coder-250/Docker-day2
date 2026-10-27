# 02 — Python web app and Dockerfile

This sample uses Python's built-in HTTP server, so no third-party packages are required.

## Build
Run these commands from this folder:
```bash
docker build -t day2-python-app .
```

## Run
```bash
docker run --name day2-python-demo -d -p 8000:8000 day2-python-app
```
Open http://localhost:8000.

## Configure the message
```bash
docker rm -f day2-python-demo
docker run --name day2-python-demo -d -p 8000:8000 -e APP_MESSAGE="Hello, Docker workshop!" day2-python-app
```
Refresh the page to see the message.

## Logs and cleanup
```bash
docker logs day2-python-demo
docker rm -f day2-python-demo
```
Never put real passwords, API keys, or other secrets in a Dockerfile or bake them into an image.
