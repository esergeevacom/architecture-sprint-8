import datetime
from random import randint
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import ORJSONResponse
from src.apps.reports.api.v1.schemas import (
    BaseUnprocessableResponse,
    UserReportData,
    UserReportResponse,
)
from src.base.security import get_payload

router = APIRouter()

USER_ROLE = "prothetic_user"


@router.get(
    "",
    responses={
        "200": {"model": UserReportResponse},
        "422": {"model": BaseUnprocessableResponse},
    },
    summary="Генерация отчета",
)
async def attributes_search(
    token_data: dict[str, Any] = Depends(get_payload),
) -> ORJSONResponse:
    """
    Получение отчета
    """

    # Проверка наличия роли prothetic_user
    roles = token_data.get("realm_access", {}).get("roles", [])
    if USER_ROLE not in roles:
        raise HTTPException(status_code=403, detail="Access denied: insufficient permissions")

    report = UserReportResponse(
        user_id=token_data.get("sub"),
        report_data=UserReportData(
            battery_status=randint(10, 100), last_updated=datetime.datetime.now()
        ),
    ).model_dump()

    return ORJSONResponse(status_code=status.HTTP_200_OK, content=report)
