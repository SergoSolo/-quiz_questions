from datetime import datetime
from http import HTTPStatus

import aiohttp
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import logger
from app.crud.question import question_service


async def get_unique_questions(
        questions_num: int,
        session: AsyncSession,
        http_client: aiohttp.ClientSession
):
    """Функция получние уникальных вопросов от запроса к API."""
    unique_questions = []
    url = (
            "https://jservice.io/api/random?count="
            f"{questions_num - len(unique_questions)}"
    )
    while questions_num > len(unique_questions):
        questions = await http_client.get(url)
        if questions.status == HTTPStatus.OK:
            questions = await questions.json()
            for question in questions:
                question = await question_service.get_object_by_question_id(
                    question["id"],
                    session
                )
                if question is not None:
                    logger.info(
                        (
                            "Производим повторный запрос для ",
                            "получения уникального вопроса."
                        )
                    )
                unique_questions.append(
                        {
                            "question_id": question["id"],
                            "question": question["question"],
                            "answer": question["answer"],
                            "created_at": datetime.strptime(
                                question["created_at"],
                                "%Y-%m-%dT%H:%M:%S.%fZ"
                            )
                        }
                    )
        else:
            raise HTTPException(
                status_code=questions.status,
                detail="API недоступен."
            )
    return unique_questions
