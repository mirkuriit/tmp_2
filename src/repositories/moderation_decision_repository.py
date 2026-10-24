from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.moderation_decision import ModerationDecision


class ModerationDecisionRepository:
    def __init__(self, db_session: AsyncSession):
        self._session = db_session

    async def get_one_or_none(
            self,
            moderation_decision_id: UUID,
            *,
            is_deleted: bool = False,
    ) -> ModerationDecision | None:
        filters = [
            ModerationDecision.id == moderation_decision_id,
            ModerationDecision.is_deleted == is_deleted
        ]

        return await self._session.scalar(select(ModerationDecision).where(*filters))


    async def create(self, moderation_decision: ModerationDecision) -> ModerationDecision:
        self._session.add(moderation_decision)
        await self._session.flush()
        return moderation_decision

