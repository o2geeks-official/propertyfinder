import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app: FastAPI = FastAPI()

static_path_str = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "static",
)
app.mount(
    "/social/static",
    StaticFiles(directory=static_path_str),
    name="social/static",
)
