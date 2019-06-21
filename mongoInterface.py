# python3
# mongoInterface.py — Defines an interface for mongo databases
from pymongo import *

def find_docs(project, host='localhost', port=27017, dbname='test', coll='test'):
    client = MongoClient(host='localhost', port=27017)
    db = client.video

    docs = [doc for doc in db.movieDetails.find({})]
    print(docs)
    print("Ok")
    client.close()
    return docs

def test():
    print("Wokr")

# client = MongoClient(host='localhost', port=27017)
# db = client.video

# docs = [doc for doc in db.movieDetails.find({})]
# print(docs)

# client.close()