from typing import Any

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from src.base.routes import openapi_tags, setup_routes
from src.base.settings import settings
from starlette.middleware.cors import CORSMiddleware


def build_app() -> FastAPI:
    app_params: dict[str, Any] = {
        "title": settings.project_name,
        "version": settings.environment,
        "default_response_class": ORJSONResponse,
        "openapi_tags": openapi_tags,
    }
    app = FastAPI(**app_params)

    setup_routes(app)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[settings.frontend_app_api_url],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app
