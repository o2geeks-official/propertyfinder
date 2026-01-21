from fastapi import FastAPI
from propertyfinder_api.api.routers.auth import router as auth_router

app = FastAPI(title="PropertyFinder API")

app.include_router(auth_router)

@app.get("/health")
def health():
    return {"status": "ok"}
