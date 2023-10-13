import aiohttp
from fastapi import APIRouter, Depends, Query
from fastapi_pagination import Page, paginate
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_http_client_session
from app.core.db import get_async_session
from app.crud.question import question_service
from app.schemas import QuestionSchemaDB
from app.service import get_unique_questions

router = APIRouter()


@router.post(
        "/",
        summary="Запрос на получение вопросов к викторине.",
        response_model=list | QuestionSchemaDB
)
async def request_for_questions(
    questions_num: int = Query(
        None,
        gt=0,
        le=100,
        description="Необходимое количество вопросов."
    ),
    session: AsyncSession = Depends(get_async_session),
    http_client: aiohttp.ClientSession = Depends(get_http_client_session)
):
    """
    Для получения информации необходимо ввести:

    - **questions_num**: необходимое количество вопросов(за раз максимум 100).
    """
    questions = await get_unique_questions(questions_num, session, http_client)
    await question_service.create_object(questions, session)
    db_object = await question_service.get_previous_object(session)
    return db_object if db_object else []


@router.get(
        "/get_all",
        summary="Получить все записанные вопросы к викторине.",
        response_model=Page[QuestionSchemaDB]
)
async def get_all_questions(
        session: AsyncSession = Depends(get_async_session)
) -> Page[QuestionSchemaDB]:
    """
    Вы можете получить все записанные вопросы.

    - **page**: Номер страницы (Опционально)
    - **size**: Количество данных выводимых на странице (Опционально)
    """
    questions = await question_service.get_multi(session)
    return paginate(questions)
