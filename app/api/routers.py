from fastapi import APIRouter

from app.api.endpoints import question_router

main_router = APIRouter(prefix="/api")

main_router.include_router(
    question_router,
    prefix="/question",
    tags=["Работа с вопросами к викторине."]
)
