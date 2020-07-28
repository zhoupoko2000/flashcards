from flask import jsonify
from pymongo import MongoClient
# from bson.objectid import ObjectId
# client = MongoClient('192.168.33.11', 27017)
client = MongoClient(host="mongodb://mongo-0.mongo,mongo-1.mongo,mongo-2.mongo", port="27017")
dbfoo = client.foo


def save_db(record):
    return dbfoo.foo.insert_one(record)


def remove_db(record):
    return dbfoo.foo.delete_one({"_id": record['_id']})


def load_db():
    output = []
    my_cursor = dbfoo.foo.find().sort("_id", 1).limit(50)
    for s in my_cursor:
        output.append({'question': s['question'], 'answer': s['answer'], '_id': s['_id']})
    return output


# db = load_db()
# db.foo.insertMany([{"question": "Hello (formal)", "answer":
# "\u0417\u0434\u0440\u0430\u0432\u0441\u0442\u0432\u0443\u0439\u0442\u0435"}, {"question": "Goodbye (formal)",
# "answer": "\u0414\u043e \u0441\u0432\u0438\u0434\u0430\u043d\u0438\u044f"}, {"question": "Hello (informal)",
# "answer": "\u041f\u0440\u0438\u0432\u0435\u0442"}, {"question": "Goodbye (informal)", "answer":
# "\u041f\u043e\u043a\u0430"}, {"question": "how are you", "answer": "fine"}])
