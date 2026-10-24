from src.models.moderation_decision import ModerationDecision
from src.schemas.moderation_decision_schema import (
    ModerationDecisionCreate,
    ModerationDecisionResponse,
)


class ModerationDecisionMapper:
    @staticmethod
    def schema_to_model(data: ModerationDecisionCreate) -> ModerationDecision:
        return ModerationDecision(
            **data.model_dump()
        )

    @staticmethod
    def model_to_schema(data: ModerationDecision) -> ModerationDecisionResponse:
        return ModerationDecisionResponse.model_validate(data)