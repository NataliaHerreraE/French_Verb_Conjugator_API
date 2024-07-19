from pymongo import MongoClient
from .db import Database
import app_config as config

##pip install pymongo
#database = MongoClient("mongodb+srv://dbuser:LIuVZsr0Hkmxyj9t@clusterfrenchverb.emnl5gp.mongodb.net/?retryWrites=true&w=majority&appName=ClusterFrenchVerb")

conn = Database(connection_string=config.CONST_MONGO_URL, database_name=config.CONST_DATABASE)
conn.connect()



