# python3
# mongoInterface.py — Defines an interface for mongo databases
from pymongo import *

class MongoInterface:
    def __init__(self, host='localhost', port=27017, dbname='test'):
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client[dbname]

    def find_docs(self, coll='test', project={}):
        db = self.db

        docs = [doc for doc in db[coll].find({}, projection=project)]
        return docs

    def close_conn(self):
        self.client.close()
