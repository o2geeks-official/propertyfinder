import os

import uvicorn

from propertyfinder_api.config import server as server_settings

if __name__ == "__main__":
    log_level = os.getenv(
        "LOG_LEVEL",
        "error",
    ).lower()  # Default to 'error' if not set, allowed values: 'debug', 'info', 'warning', 'error', 'critical'
    uvicorn.run(
        "edyouapp_api.app:app",
        host=server_settings.HOST,
        port=server_settings.PORT,
        proxy_headers=True,
        forwarded_allow_ips="*",
        reload=server_settings.DEBUG,
        log_level=log_level,
    )
