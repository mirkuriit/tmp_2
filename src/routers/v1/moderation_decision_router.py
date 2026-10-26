from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Depends
from starlette import status

from src.dependencies.moderation_decision_dependency import \
   moderation_decision_service_dependency
from src.infrastructure.db.dependencies import get_read_session, get_session
from src.schemas.moderation_decision_schema import (
   ModerationDecisionCreate,
   ModerationDecisionResponse,
)
from src.services.moderation_decision_service import (
   ModerationDecisionService,
)

router = APIRouter(prefix="/moderation_decision/v1", tags=["Moderation V1"])


@router.post("", status_code=status.HTTP_201_CREATED)
async def create_moderation_decision(
        data: ModerationDecisionCreate,
        moderation_decision_service: Annotated[ModerationDecisionService, Depends(moderation_decision_service_dependency(get_session))]
) -> ModerationDecisionResponse:
   return await moderation_decision_service.create(data)


@router.get("/{moderation_decision_id}")
async def get_moderation_decision(
        moderation_decision_id: UUID,
        moderation_decision_service: Annotated[ModerationDecisionService, Depends(moderation_decision_service_dependency(get_read_session))]
) -> ModerationDecisionResponse:
   return await moderation_decision_service.get_one(moderation_decision_id)



