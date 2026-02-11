from fastapi import FastAPI
from fastapi.responses import FileResponse # Import this
import os
from pydantic import BaseModel

app = FastAPI()

class Payload(BaseModel):
    text_content: str

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
    file_path = "dummy_guide.pdf"
    
    # Check if file exists to avoid crashing
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path, 
            filename="my_cool_guide.pdf", # Name the user sees when downloading
            media_type="application/pdf"
        )
    else:
        return {"error": "File not found on server"}

@app.post("/api/print-payload")
def print_payload(payload: Payload):
    # This prints the string to your terminal/console logs
    print(f"Received Payload: {payload.text_content}")
    
    # Return a confirmation to the client
    return {
        "status": "success", 
        "received_data": payload.text_content
    }
