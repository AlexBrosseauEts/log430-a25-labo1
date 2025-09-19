from pymongo import MongoClient
import os

class UserDAOMongo:
    def __init__(self):
        host = os.getenv("MONGODB_HOST", "localhost")
        self.client = MongoClient(f"mongodb://{host}:27017/")
        self.db = self.client["store_manager"]
        self.collection = self.db["users"]

    def select_all(self):
        return list(self.collection.find())

    def insert(self, user):
        self.collection.insert_one(user.__dict__)

    def update(self, user):
        self.collection.update_one({"id": user.id}, {"$set": user.__dict__})

    def delete(self, user_id):
        self.collection.delete_one({"id": user_id})