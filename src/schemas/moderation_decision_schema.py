from uuid import UUID

from src.schemas.base_schema import Base


class ModerationDecisionBase(Base):
    comment: str
    is_allowed: bool


class ModerationDecisionCreate(ModerationDecisionBase):
    pass


class ModerationDecisionResponse(ModerationDecisionBase):
    id: UUID