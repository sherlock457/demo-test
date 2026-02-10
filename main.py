from fastapi import FastAPI
from fastapi.responses import FileResponse # Import this
import os

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

@app.get("/api/download-pdf")
def get_pdf():
    file_path = "The_Fermi_Paradox.pdf"
    
    # Check if file exists to avoid crashing
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path, 
            filename="my_cool_guide.pdf", # Name the user sees when downloading
            media_type="application/pdf"
        )
    else:
        return {"error": "File not found on server"}
