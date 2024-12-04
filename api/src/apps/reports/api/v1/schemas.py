from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field


class UserReportData(BaseModel):
    battery_status: float = Field(..., description="Статус заряда батареи", gt=0, le=100)
    last_updated: datetime


class UserReportResponse(BaseModel):
    user_id: str = Field(..., description="Идентификатор пользователя")
    report_data: UserReportData


class BaseErrorResponse(BaseModel):
    id: Optional[int] = Field(None, title="Числовой код ошибки")
    code: str = Field(title="Символьный код ошибки (на латинице без пробелов)")
    source: Optional[Any] = Field(None, title="Источник ошибки")
    title: Optional[str] = Field("", title="Заголовок ошибки")
    detail: str = Field(title="Описание ошибки")


class BaseUnprocessableResponse(BaseModel):
    errors: list[BaseErrorResponse]
    meta: Optional[dict[Any, Any]] = Field(None)
    data: Optional[dict[Any, Any]] = Field(None)
