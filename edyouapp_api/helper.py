import math
import os
import random
import re
from typing import Any

from edyouapp_api.api.models.common import (
    BaseStandardResponse,
)


def generate_otp() -> str:
    if os.getenv("APP_MODE") == "staging" or os.getenv("APP_MODE") == "dev":
        return "1111"
    digits = "0123456789"
    otp = ""
    for _i in range(4):
        otp += digits[math.floor(random.random() * 10)]
    print(f"OPT generated for Signup or Reset Password {otp}")
    return otp


def base_standard_response(
    data=None,
    status_code: int = 200,
    success: bool = True,
    detail: str = "",
) -> BaseStandardResponse:
    return BaseStandardResponse(
        status_code=status_code,
        success=success,
        detail=detail,
        data=data,
    )


def strip_none_from_dict(data) -> Any | None:
    if isinstance(data, dict):
        return {
            k: strip_none_from_dict(v)
            for k, v in data.items()
            if k is not None and v is not None
        }
    elif isinstance(data, list):
        return [strip_none_from_dict(item) for item in data if item is not None]
    elif isinstance(data, tuple):
        return tuple(strip_none_from_dict(item) for item in data if item is not None)
    elif isinstance(data, set):
        return {strip_none_from_dict(item) for item in data if item is not None}
    else:
        return data


def slugify(s):
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    s = re.sub(r"^-+|-+$", "", s)
    return s
