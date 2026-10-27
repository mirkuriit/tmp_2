from uuid import UUID

from fastapi.exceptions import HTTPException
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

    async def create(self, moderation_decision: ModerationDecisionCreate, idempotency_key: UUID) -> ModerationDecisionResponse:
        wanted_moderation_decision = await self._repository.get_by_idempotency_key(idempotency_key)
        if wanted_moderation_decision:
            return self._mapper.model_to_schema(wanted_moderation_decision)
        created_moderation_decision = await self._repository.create(
            self._mapper.schema_to_model(moderation_decision, idempotency_key)
        )
        return self._mapper.model_to_schema(created_moderation_decision)