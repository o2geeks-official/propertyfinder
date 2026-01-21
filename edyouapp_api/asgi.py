from contextlib import asynccontextmanager

import bugsnag
from bugsnag.asgi import BugsnagMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from loguru import logger

from edyouapp_api.api.services.institutes import institute_service
from edyouapp_api.config import settings
from edyouapp_api.config.bugsnag import bugsnag as bugsnag_settings
from edyouapp_api.config.security import Security
from edyouapp_api.db.mongodb import MongoDB
from edyouapp_api.exceptions import attach_exception_handler
from edyouapp_api.log import init_logging

bugsnag.configure(
    api_key=bugsnag_settings.BUGSNAG_API_KEY,
    release_stage=bugsnag_settings.BUGSNAG_RELEASE_STAGE,
)

# Authentication dependency
API_KEY_NAME = "EDYOU-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

# Instantiate your Security settings
security_settings = Security()


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_logging()
    await MongoDB.connect()
    await institute_service.save_schools_by_state()
    yield
    await MongoDB.disconnect()


def get_application() -> FastAPI:
    """Initialize FastAPI application."""
    logger.debug("Initialize FastAPI application node.")
    app = FastAPI(
        title=settings.PROJECT_NAME,
        debug=settings.DEBUG,
        version=settings.VERSION,
        openapi_url=settings.OPENAPI_URL,
        lifespan=lifespan,
    )

    # Wrap your ASGI app with Bugsnag
    app.add_middleware(BugsnagMiddleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    attach_exception_handler(app=app)
    logger.debug(f"Swagger Api Docs can be viewed at -> {settings.SWAGGER_API_URL}")
    return app
