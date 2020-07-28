import pymongo
import pprint
from pymongo import MongoClient
client = MongoClient('192.168.33.11', 27017)
db=client.foo
for c in db.foo.find():
    pprint.pprint(c)

# record =

query = {"_id": record['_id'])}
dbfoo.foo.deleteOne({"_id": ObjectId(record['_id'])})