"""Application configuration.

The ``config`` submodule defines configuration for your application, and more.

"""

from edyouapp_api.config.apns import apns_settings
from edyouapp_api.config.application import settings
from edyouapp_api.config.bugsnag import bugsnag
from edyouapp_api.config.ejabberd import ejabberd
from edyouapp_api.config.livekit import livekit
from edyouapp_api.config.mongo import mongo
from edyouapp_api.config.redis import redis
from edyouapp_api.config.security import security
from edyouapp_api.config.server import server

__all__ = (
    "settings",
    "redis",
    "mongo",
    "server",
    "bugsnag",
    "ejabberd",
    "livekit",
    "security",
    "apns_settings",
)
