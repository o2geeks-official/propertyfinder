from typing import Optional
from bson import ObjectId
from propertyfinder_api.db.mongo import users_collection
from propertyfinder_api.api.models.user import UserCreate, UserInDB

async def get_user_by_email(email: str) -> Optional[UserInDB]:
    doc = await users_collection.find_one({"email": email})
    if not doc:
        return None
    return UserInDB(**doc)

async def create_user(user: UserCreate, hashed_password: str) -> str:
    user_dict = {"email": user.email, "hashed_password": hashed_password}
    result = await users_collection.insert_one(user_dict)
    return str(result.inserted_id)
