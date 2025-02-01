# Project README - FastAPI Endpoint for Information Retrieval

This project aims to create and host an HTTP endpoint that provides specific information in JSON format based on query parameters. The endpoint is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python.

## Table of Contents

- [Requirements](#requirements)
- [Acceptance Criteria](#acceptance-criteria)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Requirements

The endpoint is expected to provide the following information in JSON format:

```json
{
  "email" : email,
  "utc_time": "2023-08-21T15:04:05Z",
  "github_repo_url": "https://github.com/username/repo",
  "status_code": 200
}

## Backlink
    https://hng.tech.hire/python-developers



'''




# Deploy FastAPI on Render

Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render.

See https://render.com/docs/deploy-fastapi or follow the steps below:

## Manual Steps

1. You may use this repository directly or [create your own repository from this template](https://github.com/render-examples/fastapi/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

Or simply click:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/render-examples/fastapi)

## Thanks

Thanks to [Harish](https://harishgarg.com) for the [inspiration to create a FastAPI quickstart for Render](https://twitter.com/harishkgarg/status/1435084018677010434) and for some sample code!
