from typing import Optional

from fastapi import FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

@app.get("/")
async def root():
    return {"message": "Welcome to my HNG Api"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get('/hng')
def get_data():
    email = 'thrilltim@gmail.com'
    current_datetime =  datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    github_repo_url = "https://github.com/kaymohh/HNG"

    current_day = datetime.now().strftime("%A")

    return {
        'email' : email,
        'current_datetime' : current_datetime,
        'github_repo_url' : github_repo_url,
        "status_code": 200,

    }
