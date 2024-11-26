import mysql.connector
from mysql.connector import Error

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="api_usuarios"
    )
    if connection.is_connected():
        return connection
    else:
        raise Exception("Erro ao conectar ao banco de dados!")
