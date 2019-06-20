import pymongo
from decouple import config
from bson.objectid import ObjectId

mongo_url = config('MONGO_URL')


def new_connection(collection):
    client = pymongo.MongoClient(mongo_url)
    db = client["extracoes"]
    collection = db[collection]
    return collection, client


def get_process(collection):
    collection, _ = new_connection(collection)
    return list(collection.find({}))


def update_process(_id, processo, collection):
    collection, client = new_connection(collection)
    _id = ObjectId(_id)

    query = {"_id": _id}
    processo['_id'] = _id

    new_value = {"$set": processo}
    collection.update_one(query, new_value)
    client.close()
