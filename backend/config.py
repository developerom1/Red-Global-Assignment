import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # File storage
    UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./uploads")
    MAX_FILE_SIZE = 500 * 1024 * 1024  # 500MB
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./meetings.db")
    
    # Ollama settings
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama2")
    
    # ChromaDB
    CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "./.chromadb")
    
    # Whisper
    WHISPER_MODEL = os.getenv("WHISPER_MODEL", "base")
    
    # CORS
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")

settings = Settings()

# Create directories if they don't exist
os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
os.makedirs(settings.CHROMA_PERSIST_DIR, exist_ok=True)
