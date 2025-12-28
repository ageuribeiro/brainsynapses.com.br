from pymongo import MongoClient
import os

def get_db():
    client = MongoClient(os.environ["MONGO_URI"])
    return client["brainsynapses"]