"""
Transfer News Model Definition
Captures breaking scoops, tactical analysis wires, and official signings.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class TransferNews(Base):
    __tablename__ = "transfer_news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, index=True)
    description = Column(Text, nullable=False)
    content = Column(Text, nullable=True)
    image_url = Column(String(500), nullable=True)

    player_id = Column(Integer, ForeignKey("players.id"), nullable=True, index=True)
    club_id = Column(Integer, ForeignKey("clubs.id"), nullable=True, index=True)

    source = Column(String(150), nullable=False, default="BlueLock Intelligence Wire")
    source_url = Column(String(500), nullable=True)
    published_at = Column(DateTime, default=datetime.utcnow, index=True)
    category = Column(String(50), default="Negotiation", index=True) # Confirmed, Rumour, Negotiation, Loan, Free Transfer
    reliability_score = Column(Integer, default=85) # 1 - 100
    read_time = Column(String(30), default="3 min read")
    ego_impact = Column(String(100), nullable=True)

    # Relationships
    player = relationship("Player", back_populates="news_items")
    club = relationship("Club", back_populates="news_items")
