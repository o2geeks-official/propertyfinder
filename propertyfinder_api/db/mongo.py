from motor.motor_asyncio import AsyncIOMotorClient
import os
from propertyfinder_api.db.client import db

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "propertyfinder")

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

users_collection = db.get_collection("users")
