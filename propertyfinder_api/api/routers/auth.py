from fastapi import APIRouter, HTTPException, Depends
from propertyfinder_api.api.enum.auth import UserCreate, UserLogin, Token
from propertyfinder_api.api.services.auth import create_user, authenticate_user, create_token
from propertyfinder_api.db.client import db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=Token)
async def register(data: UserCreate):
    existing = await db.users.find_one({"email": data.email})
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = await create_user(data.email, data.password)
    token = create_token({"sub": str(user["_id"])})
    return {"access_token": token}

@router.post("/login", response_model=Token)
async def login(data: UserLogin):
    user = await authenticate_user(data.email, data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token({"sub": str(user["_id"])})
    return {"access_token": token}
