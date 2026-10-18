# CI/CD Pipeline Demo (Flask + Docker + GitHub Actions)

A small Flask app that is automatically tested, built into a Docker image,
and pushed to Docker Hub every time code is pushed to GitHub.

## Pipeline flow

```
git push -> GitHub Actions -> run tests -> build Docker image -> push to Docker Hub
```

## Project files

| File | Purpose |
|------|---------|
| `app.py` | Flask web app |
| `test_app.py` | Automated tests (run in the pipeline) |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Instructions to build the container image |
| `.github/workflows/ci.yml` | The CI/CD pipeline |

## Run locally

```
docker build -t myapp .
docker run -p 5000:5000 myapp
curl http://localhost:5000
```

## One-time GitHub setup

1. Create a Docker Hub access token (Account Settings -> Personal access tokens).
2. In your GitHub repo: Settings -> Secrets and variables -> Actions, add:
   - `DOCKERHUB_USERNAME` = your Docker Hub username
   - `DOCKERHUB_TOKEN` = the token you created

## Live demo steps

1. Edit `app.py` and change "Version 1" to "Version 2".
2. Push the change:
   ```
   git add .
   git commit -m "Update to version 2"
   git push
   ```
3. Open the Actions tab on GitHub and show the pipeline running (test, then build-and-push).
4. In the terminal, pull and run the new image:
   ```
   docker pull YOURNAME/myapp:latest
   docker run -p 5000:5000 YOURNAME/myapp:latest
   curl http://localhost:5000
   ```
   The output should now say "Version 2".
