# 04 — Day 2 practice challenges

## Challenge 1: Customize the app
1. Change the heading in `02-python-web-app/app.py`.
2. Build an image named `my-first-image`.
3. Run it on host port `8002`.
4. Open http://localhost:8002.

## Challenge 2: Environment variables
1. Run the app with a custom `APP_MESSAGE`.
2. Change the message without editing the source code.
3. Explain why you recreate the container to change its environment variable.

## Challenge 3: Dockerfile instructions
Explain `FROM`, `WORKDIR`, `COPY`, `ENV`, `EXPOSE`, and `CMD` in your own words.

## Challenge 4: Troubleshooting
Diagnose a busy host port, an existing container name, a build from the wrong directory, and a browser that cannot reach the app.

Useful commands:
```bash
docker ps -a
docker logs CONTAINER_NAME
docker images
```

## Completion checklist
- [ ] I can explain each Dockerfile instruction.
- [ ] I can build an image.
- [ ] I can run the container and open the app.
- [ ] I can configure a runtime environment variable.
- [ ] I can inspect logs and clean up containers.
