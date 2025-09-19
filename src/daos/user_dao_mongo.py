from pymongo import MongoClient
import os
from models.user import User
class UserDAOMongo:
    def __init__(self):
        env_path = "../.env"
        print(os.path.abspath(env_path))
        load_dotenv(dotenv_path=env_path)
        host = os.getenv("MONGODB_HOST", "mongo")
        db_name = os.getenv("MONGO_DB_NAME", "mydb")
        username = os.getenv("MONGO_USERNAME", "user")
        password = os.getenv("MONGO_PASSWORD", "pass")
        uri = f"mongodb://{username}:{password}@{host}:27017/?authSource=admin"
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.col = self.db["users"]
    ##-------------Traduction Mongo <-> MySql -------------##
    def _doc_to_user(self, doc):
        #transformer doc mongo en User object
        return User(id=str(doc["_id"]), name=doc.get("name"), email=doc.get("email"))

    def _user_to_doc(self, user: User):
        # le contraire de l'autre
        return {"name": user.name, "email": user.email}

    ##-------------    Opération normales    -------------##
    def select_all(self):
        docs = self.col.find()
        return [self._doc_to_user(d) for d in docs]

    def insert(self, user: User):
        res = self.col.insert_one(self._user_to_doc(user))
        return str(res.inserted_id)

    def update(self, user: User):
        if not user.id:
            raise ValueError("user.id requis pour update")
        self.col.update_one(
            {"_id": ObjectId(user.id)},
            {"$set": self._user_to_doc(user)}
        )

    def delete(self, user_id):
        self.col.delete_one({"_id": ObjectId(user_id)})