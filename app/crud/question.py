from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Question


class CRUDQuesttion:
    """Класс для работы с базой данных."""

    def __init__(self, model) -> None:
        self.model = model

    async def get_previous_object(
            self,
            session: AsyncSession
    ):
        db_object = await session.execute(
            select(self.model).order_by(
                self.model.id.desc()
            ).offset(1).limit(1)
        )
        return db_object.scalars().first()

    async def get_object_by_question_id(
            self,
            question_id: int,
            session: AsyncSession
    ):
        db_object = await session.execute(
            select(self.model).where(
                self.model.question_id == question_id
            )
        )
        return db_object.scalars().first()

    async def create_object(
            self,
            objects_in: list[dict],
            session: AsyncSession
    ):
        await session.execute(
            insert(self.model),
            objects_in
        )
        await session.commit()


question_service = CRUDQuesttion(Question)
