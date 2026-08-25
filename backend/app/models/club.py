"""
Club Model Definition
"""

from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from app.database import Base

class Club(Base):
    __tablename__ = "clubs"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    name = Column(String(150), nullable=False, index=True)
    short_name = Column(String(20), nullable=True)
    country = Column(String(100), nullable=False)
    flag = Column(String(20), nullable=True, default="🌍")
    league = Column(String(100), nullable=False, index=True)
    stadium = Column(String(150), nullable=True)
    logo_url = Column(String(500), nullable=True)
    squad_value = Column(String(50), nullable=True)
    squad_value_raw = Column(Float, nullable=True, default=0.0) # in Millions EUR
    transfer_budget = Column(String(50), nullable=True)
    transfer_budget_raw = Column(Float, nullable=True, default=0.0) # in Millions EUR
    wage_bill = Column(String(50), nullable=True)
    manager = Column(String(100), nullable=True)
    president = Column(String(100), nullable=True)
    ego_rank = Column(String(100), nullable=True)
    description = Column(Text, nullable=True)

    # Attribution & Trademark Metadata
    trademark_notice = Column(String(255), nullable=True, default="Club crest, name and trademarks belong to the respective football club.")
    source = Column(String(150), nullable=True, default="Official Club Register")
    source_url = Column(String(500), nullable=True)

    # Relationships
    players = relationship("Player", back_populates="current_club", foreign_keys="Player.current_club_id")
    incoming_transfers = relationship("Transfer", back_populates="interested_club", foreign_keys="Transfer.interested_club_id")
    outgoing_transfers = relationship("Transfer", back_populates="current_club", foreign_keys="Transfer.current_club_id")
    news_items = relationship("TransferNews", back_populates="club")
