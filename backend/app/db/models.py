from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.db.session import Base

class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True)
    url = Column(Text, nullable=False, unique=True)
    title = Column(Text, nullable=False)
    source = Column(Text)
    published_at = Column(TIMESTAMP)
    ingested_at = Column(TIMESTAMP, default=lambda:datetime.now(timezone.utc), nullable=False)
    summary = relationship("Summary", back_populates="article", uselist=False, cascade="all")

class Summary(Base):
    __tablename__ = "summaries"
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    content = Column(Text, nullable=False)
    article = relationship("Article", back_populates="summary")


