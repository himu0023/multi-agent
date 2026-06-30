from fastapi import FastAPI

app = FastAPI(
    title="Customer Support AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Customer Support AI Backend"
    }