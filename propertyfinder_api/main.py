from fastapi import FastAPI
from propertyfinder_api.api.routers import auth

app = FastAPI(title="PropertyFinder API")

app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Welcome to PropertyFinder API"}
