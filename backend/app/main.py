from fastapi import FastAPI

# Correct import path for user_router.py
from app.api.routes.user_router import router as user_router

app = FastAPI(
    title="Customer Support AI",
    version="1.0.0"
)

app.include_router(user_router)

@app.get("/")
def home():
    return {
        "message": "Customer Support AI Backend"
    }