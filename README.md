# FastAPI Endpoint for Information Retrieval

This project provides an HTTP endpoint that returns specific information in JSON format based on query parameters. The endpoint is built using FastAPI, a modern, high-performance web framework for building APIs with Python.

## Table of Contents

- [Requirements](#requirements)
- [Acceptance Criteria](#acceptance-criteria)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Requirements

The API endpoint should return the following JSON response:

```json
{
  "email": "example@example.com",
  "utc_time": "2023-08-21T15:04:05Z",
  "github_repo_url": "https://github.com/username/repo",
  "status_code": 200
}
```

### Backlink
[Hire Python Developers](https://hng.tech.hire/python-developers)

---

# Deploying FastAPI on Render

This project provides a template for deploying a FastAPI service on Render.

For detailed documentation, refer to: [Render FastAPI Deployment Guide](https://render.com/docs/deploy-fastapi).

## Deployment Steps

1. Use this repository directly or [create a new repository from this template](https://github.com/render-examples/fastapi/generate) to customize the code.
2. Create a new **Web Service** on Render.
3. Provide the repository URL (your own or this template).
4. Render will automatically detect the Python environment and install dependencies using `pip`.
5. Set the **Start Command** as follows:

    ```sh
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click **Create Web Service** to complete the deployment.

### One-Click Deployment

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/render-examples/fastapi)


