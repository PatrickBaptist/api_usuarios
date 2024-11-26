from db import create_connection, close_connection

def criar_usuario(nome, cpf, cep):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            query = "INSERT INTO usuarios (nome, cpf, cep) VALUES (%s, %s, %s)"
            values = (nome, cpf, cep)
            cursor.execute(query, values)
            connection.commit()
            print("Usuário criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
        finally:
            cursor.close()
            close_connection(connection)
