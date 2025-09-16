# github-gist-api

<!--
README for the GitHub Gist API project.
This project provides a FastAPI-based HTTP API to fetch public Gists for any GitHub user.
-->

A simple Python HTTP API that fetches a GitHub user's public Gists using the GitHub API.

## Features
- Endpoint: `/USERNAME` returns a list of public Gists for the specified GitHub user.
- Automated tests using pytest and httpx.
- Dockerized for easy deployment (listens on port 8080).

## Usage

### 1. Install dependencies
```sh
pip install -r requirements.txt
```

### 2. Run the server
```sh
uvicorn src.main:app --host 0.0.0.0 --port 8080
```

## How to Test the Application

You can test the application in two ways:

### 1. Run Automated Tests
Run the following command to execute all automated tests:
```sh
pytest
```
This will run the test suite in the `tests/` directory and verify the API works as expected (e.g., using the example user `octocat`).

### 2. Manual API Testing
After starting the server, you can test the API manually:
- Open your browser or use a tool like `curl` or Postman.
- Make a GET request to:
  - `http://localhost:8080/octocat`
- You should receive a JSON list of public Gists for the user `octocat`.

### 3. Dockerized Testing
You can also run tests inside the Docker container:
```sh
docker run github-gist-api pytest
```

### 4. Build and Run with Docker
To build the Docker image and run the container:
```sh
docker build -t github-gist-api .
docker run -p 8080:8080 github-gist-api
```

### 5. Interactive API Docs
FastAPI provides interactive docs at:
- `http://localhost:8080/docs` (Swagger UI)

## Example
GET http://localhost:8080/octocat
