import os
import base64
from fastapi import FastAPI
from fastapi.responses import JSONResponse,Response

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
def get_pdf_base64_raw():
    file_path = "dummy_guide.pdf"
    
    if os.path.exists(file_path):
        # 1. Read file bytes
        with open(file_path, "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            
        # 2. Encode to Base64 string
        base64_string = base64.b64encode(pdf_bytes).decode('utf-8')
        
        # 3. Return ONLY the string as plain text
        return Response(content=base64_string, media_type="text/plain")
        
    else:
        return Response(content="File not found", status_code=404)
