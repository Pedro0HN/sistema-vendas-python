import mysql.connector

def conectar():
    return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'Pedroneves1@',
        database = 'banco_python',
    )