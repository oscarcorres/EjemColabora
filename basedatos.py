from pymongo import MongoClient
from pprint import pprint
cliente=MongoClient()
db=cliente.get_database("test")
coleccion=db.get_collection("users")
resultados=coleccion.find()
pprint(resultados)