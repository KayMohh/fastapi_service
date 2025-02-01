from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from typing import Union
from datetime import datetime
from fastapi.responses import JSONResponse

app = FastAPI(
    title="My API",
    description="This is a sample FastAPI application for HNG internship.",
    version="1.0.0",
    default_response_class=JSONResponse
)  # Create an instance of FastAPI

# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Allowed HTTP methods
    allow_headers=["*"],  # Allow all headers
)
@app.get("/")
async def root():
    return {"message": "Welcome to my HNG Api"}

@app.get('/hng')
def get_data():
    email = 'thrilltim@gmail.com'
    current_datetime =  datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    github_repo_url = "https://github.com/KayMohh/fastapi_service"

      return {
        'email' : email,
        'current_datetime' : current_datetime,
        'github_url' : github_repo_url,
      
    }
      return JSONResponse(content=data)
