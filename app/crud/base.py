from typing import TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

DatabaseModel = TypeVar("DatabaseModel")


class CRUDBase:
    """Базовый класс для работы с моделями."""

    def __init__(self, model):
        self.model = model

    async def get_multi(
            self,
            session: AsyncSession
    ) -> list[DatabaseModel]:
        db_objects = await session.execute(select(self.model))
        return db_objects.scalars().all()
