# AI Meeting Intelligence Platform

This is an AI-powered platform for processing and analyzing meeting recordings using advanced machine learning models.

## Features

- **File Upload**: Upload meeting recordings in MP4, WAV, or MP3 formats
- **Automatic Transcription**: Uses OpenAI Whisper for accurate speech-to-text conversion
- **Meeting Summarization**: Generates concise summaries using Ollama LLM
- **Sentiment Analysis**: Analyzes emotional tone throughout the meeting
- **Vector Search**: Semantic search capabilities using ChromaDB for finding relevant content
- **Web Interface**: Clean, responsive frontend for easy interaction
- **REST API**: FastAPI backend with comprehensive endpoints

## URLs

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs (FastAPI auto-generated)

## Prerequisites

- Python 3.8+
- Ollama installed and running for summarization
- Git

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/developerom1/Red-Global-Assignment.git
cd Red-Global-Assignment
```

2. **Install Python dependencies**
```bash
pip install -r backend/requirements.txt
```

3. **Start Ollama service** (if using summarization)
```bash
ollama serve
```

4. **Run the backend**
```bash
uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
```

5. **Run the frontend** (in a separate terminal)
```bash
python -m http.server 3000 --directory frontend
```

## API Endpoints

- **GET /**: Root endpoint
- **GET /health**: Health check
- **GET /meetings**: List all meetings
- **POST /upload**: Upload and process meeting recording

## Error Fixes

### What Was Done

- **Directory Structure**: Reorganized the deeply nested chromadb/services folders that were causing import issues
- **Import Errors**: Fixed incorrect import paths in service files (changed `from config import settings` to `from backend.config import settings`)
- **Configuration**: Updated `backend/app.py` to properly use settings from `backend/config.py` instead of hardcoded values
- **Type Safety**: Added null checks for file uploads to prevent runtime errors

## New Features Added

- **Frontend Interface**: Created a complete web interface with:
  - File upload functionality
  - Meeting list display
  - Real-time status updates
  - Responsive design with CSS
- **Service Integration**: Connected ChromaDB services for transcription, summarization, sentiment analysis, and vector search
- **CORS Support**: Added proper CORS configuration for frontend-backend communication
- **File Handling**: Implemented secure file upload with type validation

## Technical Improvements

- **Modular Architecture**: Organized code into clear backend/frontend separation
- **Error Handling**: Added comprehensive error handling throughout the application
- **Logging**: Implemented proper logging in all services
- **Database Models**: Set up SQLAlchemy models for meeting data storage
- **Vector Indexing**: Integrated ChromaDB for efficient semantic search

## Project Structure

```
Red-Global-Assignment/
├── backend/
│   ├── app.py                 # FastAPI application
│   ├── config.py              # Configuration settings
│   ├── models.py              # SQLAlchemy database models
│   ├── database.py            # Database connection
│   ├── requirements.txt       # Python dependencies
│   ├── chromadb/
│   │   ├── schemas.py        # Pydantic schemas
│   │   ├── utils.py          # Utility functions
│   │   └── services/
│   │       ├── transcription.py    # Whisper transcription service
│   │       ├── summarization.py    # Ollama summarization service
│   │       ├── sentiment.py        # Sentiment analysis service
│   │       └── vector_search.py    # ChromaDB vector search service
├── frontend/
│   ├── index.html             # Main HTML page
│   ├── styles.css             # CSS styling
│   └── app.js                 # JavaScript functionality
├── uploads/                    # Uploaded files directory
├── docs/                       # Documentation
└── README.md                   # This file
```

## Technologies Used

- **Backend**: FastAPI, SQLAlchemy, ChromaDB
- **AI/ML**: OpenAI Whisper, Ollama, PyTorch
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Database**: SQLite (configurable)
- **Vector DB**: ChromaDB

## Usage

1. Open the frontend at http://localhost:3000
2. Click "Choose File" and select a meeting recording
3. Click "Upload & Process" to start AI processing
4. View processed meetings in the meetings list
5. Use the API endpoints for programmatic access

## Future Enhancements

- User authentication and authorization
- Real-time processing status updates
- Advanced search and filtering
- Meeting participant identification
- Export functionality for summaries
- Integration with calendar applications

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License
