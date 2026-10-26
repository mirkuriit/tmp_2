from typing import Callable, Any, Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.mappers.moderation_decision_mapper import ModerationDecisionMapper
from src.repositories.moderation_decision_repository import \
    ModerationDecisionRepository
from src.services.moderation_decision_service import ModerationDecisionService


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