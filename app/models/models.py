from sqlalchemy import Column, DateTime, Integer, Text

from app.core.db import Base


class Question(Base):
    question_id = Column(Integer, nullable=False, unique=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
