from fastapi import FastAPI
from app.api.routes.user_routers import router as user_routers
from app.api.routes.chat_routes import router as chat_router

app = FastAPI(
    title="Customer Support AI",
    version="1.0.0"
)

app.include_router(chat_router)
app.include_router(user_routers)

@app.get("/")
def home():
    return {
        "message": "Customer Support AI Backend"
    }