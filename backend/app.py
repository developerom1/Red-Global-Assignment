from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
from datetime import datetime
from typing import List, Optional
import asyncio
from backend.config import settings

app = FastAPI(title="AI Meeting Intelligence Platform", version="1.0.0")

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create uploads directory if not exists
UPLOAD_DIR = settings.UPLOAD_DIR
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
async def root():
    return {"message": "AI Meeting Intelligence Platform API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.utcnow()}

# Placeholder for meetings endpoint
@app.get("/meetings")
async def get_meetings():
    return {"meetings": []}

# Placeholder for upload endpoint
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith((".mp4", ".wav", ".mp3")):
        raise HTTPException(status_code=400, detail="Unsupported file type")
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    
    # TODO: Trigger AI processing pipeline here
    
    return {
        "filename": file.filename,
        "status": "uploaded",
        "processing": "pending"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
