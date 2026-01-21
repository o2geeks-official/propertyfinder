from fastapi import APIRouter, HTTPException, status, Depends
from propertyfinder_api.api.models.user import UserCreate, UserOut, Token
from propertyfinder_api.repositories.user_repo import get_user_by_email, create_user
from propertyfinder_api.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def register_user(user: UserCreate):
    existing = await get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = hash_password(user.password)
    user_id = await create_user(user, hashed)
    return UserOut(id=user_id, email=user.email)

@router.post("/login", response_model=Token)
async def login_user(form_data: UserCreate):
    existing = await get_user_by_email(form_data.email)
    if not existing or not verify_password(form_data.password, existing.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(existing.email)
    return Token(access_token=token)
