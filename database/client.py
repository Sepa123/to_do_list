from pymongo import MongoClient
from decouple import config

# conexion local
# db_client = MongoClient().todoDB

db_client = MongoClient(config("MONGO_DB_URI")).todoDB
