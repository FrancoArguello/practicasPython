from pymongo import MongoClient

#conexion a base de datos remota
db_client = MongoClient("mongodb+srv://admin:admin1234@cluster0.6ewgtcn.mongodb.net/test").test


#conexion a base de datos local
#db_client = MongoClient().local #entre parentesis hay que poner el path a donde queremos conectarnos si no ponemos nada x defecto se conecta al localhost
                     # con el .local le apuntamos a la base de datos local

