from collections.abc import Callable
from typing import Annotated, Any
from uuid import UUID

from fastapi import Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_404_NOT_FOUND

from src.mappers.moderation_decision_mapper import ModerationDecisionMapper
from src.repositories.moderation_decision_repository import ModerationDecisionRepository
from src.schemas.moderation_decision_schema import (
    ModerationDecisionCreate,
    ModerationDecisionResponse,
)


class ModerationDecisionService:
    def __init__(
            self,
            mapper: ModerationDecisionMapper,
            repository: ModerationDecisionRepository,
    ) -> None:
        self._mapper = mapper
        self._repository = repository

    async def get_one(
            self,
            moderation_decision_id: UUID,
    ) -> ModerationDecisionResponse:
        moderation_decision = await self._repository.get_one_or_none(moderation_decision_id)
        if not moderation_decision:
            raise HTTPException(
                status_code=HTTP_404_NOT_FOUND,
                detail="Moderation decision for event not found"
            )
        return self._mapper.model_to_schema(moderation_decision)

    async def create(self, moderation_decision: ModerationDecisionCreate) -> ModerationDecisionResponse:
        created_moderation_decision = await self._repository.create(
            self._mapper.schema_to_model(moderation_decision)
        )
        return self._mapper.model_to_schema(created_moderation_decision)


def moderation_decision_service_dependency(
        session_dependency: Callable[..., Any]
) -> Callable[[AsyncSession], ModerationDecisionService]:
    def dependency(
            session: Annotated[AsyncSession, Depends(session_dependency)],
    ):
        return ModerationDecisionService(
            ModerationDecisionMapper(),
            ModerationDecisionRepository(session)
        )
    return dependency