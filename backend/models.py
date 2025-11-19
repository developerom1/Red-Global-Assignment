from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text, JSON
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Meeting(Base):
    __tablename__ = "meetings"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    uploaded_file = Column(String)
    file_format = Column(String)
    file_size = Column(Integer)
    duration = Column(Float, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Processing status
    status = Column(String, default="uploaded")  # uploaded, processing, completed, failed
    error_message = Column(Text, nullable=True)
    
    # Transcription
    transcription_text = Column(Text)
    transcription_json = Column(JSON)  # structured with timestamps
    
    # Analysis results
    summary = Column(Text)
    key_decisions = Column(JSON)
    sentiment_overall = Column(String)
    sentiment_breakdown = Column(JSON)
    topics = Column(JSON)
    knowledge_graph_json = Column(JSON)
    
    # Vector indexing
    vector_indexed = Column(Boolean, default=False)
    
    # Relationships
    action_items = relationship("ActionItem", back_populates="meeting", cascade="all, delete-orphan")
    speaker_segments = relationship("SpeakerSegment", back_populates="meeting", cascade="all, delete-orphan")

class ActionItem(Base):
    __tablename__ = "action_items"
    
    id = Column(Integer, primary_key=True, index=True)
    meeting_id = Column(Integer, ForeignKey("meetings.id", ondelete="CASCADE"))
    description = Column(Text)
    assigned_to = Column(String, nullable=True)
    due_date = Column(DateTime, nullable=True)
    priority = Column(String, default="medium")  # low, medium, high
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    meeting = relationship("Meeting", back_populates="action_items")

class SpeakerSegment(Base):
    __tablename__ = "speaker_segments"
    
    id = Column(Integer, primary_key=True, index=True)
    meeting_id = Column(Integer, ForeignKey("meetings.id", ondelete="CASCADE"))
    speaker_label = Column(String)
    start_time = Column(Float)
    end_time = Column(Float)
    text = Column(Text)
    sentiment = Column(String, nullable=True)
    
    meeting = relationship("Meeting", back_populates="speaker_segments")
