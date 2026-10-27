from uuid import UUID

from src.models.moderation_decision import ModerationDecision
from src.schemas.moderation_decision_schema import (
    ModerationDecisionCreate,
    ModerationDecisionResponse,
)


class ModerationDecisionMapper:
    @staticmethod
    def schema_to_model(data: ModerationDecisionCreate, idempotency_key: UUID) -> ModerationDecision:
        return ModerationDecision(
            **data.model_dump(),
            idempotency_key=idempotency_key
        )

    @staticmethod
    def model_to_schema(data: ModerationDecision) -> ModerationDecisionResponse:
        return ModerationDecisionResponse.model_validate(data)