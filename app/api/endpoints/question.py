import aiohttp
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import get_http_client_session
from app.core.db import get_async_session
from app.crud.question import question_service
from app.schemas.schemas import QuestionSchemaDB
from app.utils import get_unique_questions

router = APIRouter()


@router.post(
        '/',
        response_model=list | QuestionSchemaDB
)
async def get_questions(
    questions_num: int,
    session: AsyncSession = Depends(get_async_session),
    http_client: aiohttp.ClientSession = Depends(get_http_client_session)
):
    questions = await get_unique_questions(questions_num, session, http_client)
    await question_service.create_object(questions, session)
    db_object = await question_service.get_previous_object(session)
    return db_object if db_object is not None else []
