# 03 — Build, run, inspect, rebuild

Run these commands from the `02-python-web-app/` directory unless otherwise stated.

## Build and run
```bash
docker build -t day2-python-app .
docker images
docker run --name day2-python-demo -d -p 8000:8000 day2-python-app
```
Open http://localhost:8000.

## Inspect
```bash
docker ps
docker logs day2-python-demo
docker inspect day2-python-demo
docker port day2-python-demo
```

## Change the application
Edit `app.py`. A running container uses the code already copied into its image, so rebuild and recreate it:
```bash
docker rm -f day2-python-demo
docker build -t day2-python-app .
docker run --name day2-python-demo -d -p 8000:8000 day2-python-app
```

## Try a different host port
```bash
docker rm -f day2-python-demo
docker run --name day2-python-demo -d -p 8001:8000 day2-python-app
```
Open http://localhost:8001. The host port is 8001; the app still listens on container port 8000.

The `.` in `docker build` is the build context. `.dockerignore` excludes files from that context. Docker can reuse cached layers when relevant instructions and inputs have not changed.
