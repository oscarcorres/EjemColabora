from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")
citas = cliente.citas
usuario = citas.usuario
result = usuario.insert_one(
    {'nombre': 'pepe', 'contraseña': '123', 'email': 'hola@' }
)

result=usuario.find()
for item in result:
    print(item)

citas.usuario.update(
    {'nombre':'pepe'},
    {'$set':{'altura': 180, 'peso': 80, 'edad': 25, 'color_ojos': 'azul'}},
    multi=True

)
result=usuario.find()
for item in result:
    print(item)



