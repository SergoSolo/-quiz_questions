from datetime import datetime

from pydantic import BaseModel, Extra, Field


class QuestionSchema(BaseModel):
    number: int = Field(None, ge=0, le=100)

    class Config:
        extra = Extra.forbid
        schema_extra = {
            'example': {
                "questions_num": 25
            }
        }


class QuestionSchemaDB(BaseModel):
    question_id: int
    question: str
    answer: str
    created_at: datetime

    class Config:
        orm_mode = True
