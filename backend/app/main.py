from fastapi import FastAPI

# Correct import path for user_router.py
from app.api.routes.user_routers import router as user_routers

app = FastAPI(
    title="Customer Support AI",
    version="1.0.0"
)

app.include_router(user_routers)

@app.get("/")
def home():
    return {
        "message": "Customer Support AI Backend"
    }