from pydantic import BaseModel, EmailStr
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

class User(BaseModel):
    id: PyObjectId | None = None
    email: EmailStr
    hashed_password: str

    class Config:
        json_encoders = {ObjectId: str}
