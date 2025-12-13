from sqlalchemy import Column, Integer, String, Text
from ..database import Base

class Activities(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    img_url = Column(String(500), nullable=True)
