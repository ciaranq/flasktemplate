import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
# MONGODB_URI="mongodb+srv://ciaran:Code2019@quote-vj3wf.mongodb.net/quote?retryWrites=true&w=majority"
DBS_NAME = "quote"
COLLECTION_NAME = "quote"

def mongo_connect(url):
    try:c
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)