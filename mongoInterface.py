# python3
# mongoInterface.py — Define una interfaz para la recuperacion de la data
#                     almacenada en Mongo

from pymongo import *

class MongoInterface:
    """
        Módulo que permite la extracción de los datos en bruto
        de la base de datos
    """

    def __init__(self, host='localhost', port=27017, dbname='test'):
        self.client = MongoClient(host='localhost', port=27017)
        self.db = self.client[dbname]
        self.client.close()

    def find_docs(self, collec='test', f={}, p={}):
        db = self.db

        docs = [doc for doc in db[collec].find(f, p)]

        return docs

    def close_conn(self):
        self.client.close()
