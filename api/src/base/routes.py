from fastapi import FastAPI
from src.apps.reports.api.v1 import router as report_router

openapi_tags = [
    {
        "name": "reports",
        "description": "Работа с отчетами",
    },
]


def setup_routes(app: FastAPI) -> None:
    # Отчеты
    app.include_router(report_router.router, prefix="/reports", tags=["reports"])
