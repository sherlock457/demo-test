from fastapi import FastAPI

app = FastAPI()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello! The FastAPI is running. Go to /api/dummy for data."}

# Dummy data endpoint
@app.get("/api/dummy")
def get_dummy_data():
    return {
        "id": 1,
        "message": "This is a dummy response from Render using FastAPI!",
        "status": "success",
        "items": ["apple", "banana", "cherry"]
    }