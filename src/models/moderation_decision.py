from sqlalchemy.orm import Mapped

from src.infrastructure.db.base_model import AuditMixin, Base


class ModerationDecision(AuditMixin, Base):
    __tablename__ = 'moderation_decisions'
    comment: Mapped[str]
    is_allowed: Mapped[bool]