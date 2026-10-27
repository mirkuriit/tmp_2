from uuid import UUID

from sqlalchemy.orm import Mapped

from src.models.base import AuditMixin, Base


class ModerationDecision(AuditMixin, Base):
    __tablename__ = 'moderation_decisions'
    comment: Mapped[str]
    is_allowed: Mapped[bool]
    idempotency_key: Mapped[UUID]