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
        response = await http_client.get(url)
        if response.status == HTTPStatus.OK:
            response = await response.json()
            for object in response:
                question = await question_service.get_object_by_question_id(
                    object["id"],
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
                            "question_id": object["id"],
                            "question": object["question"],
                            "answer": object["answer"],
                            "created_at": datetime.strptime(
                                object["created_at"],
                                "%Y-%m-%dT%H:%M:%S.%fZ"
                            )
                        }
                    )
        else:
            raise HTTPException(
                status_code=response.status,
                detail="API недоступен."
            )
    return unique_questions
