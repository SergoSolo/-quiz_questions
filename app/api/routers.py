from fastapi import APIRouter

from app.api.endpoints import question_router

main_router = APIRouter(prefix="/api")

main_router.include_router(
    question_router,
    prefix="/questions",
    tags=["Работа с вопросами к викторине."]
)
