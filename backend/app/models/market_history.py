"""
Market Value History Model Definition
Stores chronological 5-year valuation progression for SVG charts.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base

class MarketValueHistory(Base):
    __tablename__ = "market_value_history"

    id = Column(Integer, primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=False, index=True)
    value_millions = Column(Float, nullable=False) # e.g. 180.0
    year_recorded = Column(String(20), nullable=False) # e.g. "2024" or "2024.5"
    recorded_date = Column(DateTime, default=datetime.utcnow)

    # Relationships
    player = relationship("Player", back_populates="market_history")
