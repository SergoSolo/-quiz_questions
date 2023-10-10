from sqlalchemy import Column, DateTime, Text

from app.core.db import Base


class Question(Base):
    question = Column(Text)
    answer = Column(Text)
    created_at = Column(DateTime)
