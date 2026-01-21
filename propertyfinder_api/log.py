import logging
import os
import sys

from loguru import logger

from propertyfinder_api.config import settings


class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())


def init_logging():
    uvicorn = logging.getLogger("uvicorn.access")
    for h in uvicorn.handlers:
        uvicorn.removeHandler(h)
    handler = InterceptHandler()
    uvicorn.addHandler(handler)

    # Configure loguru logger with the same log level
    log_level = os.getenv(
        "LOG_LEVEL",
        "error" if not settings.DEBUG else "debug",
    ).upper()
    logger.remove()
    logger.add(sys.stderr, level=log_level)


# Remove default handler
logger.remove()

# Set initial log level based on LOG_LEVEL env var or DEBUG setting
log_level = os.getenv("LOG_LEVEL", "error" if not settings.DEBUG else "debug").upper()
logger.add(sys.stderr, level=log_level)
