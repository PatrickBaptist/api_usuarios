from db import get_db_connection
from schemas import UsuarioCreate, UsuarioUpdate

def create_usuario(usuario: UsuarioCreate):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO usuarios (nome, cpf, cep, logradouro, bairro, cidade, estado)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (
        usuario.nome,
        usuario.cpf,
        usuario.cep,
        usuario.logradouro,
        usuario.bairro,
        usuario.cidade,
        usuario.estado
    ))
    conn.commit()
    cursor.close()
    conn.close()

def get_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    cursor.close()
    conn.close()

    return usuarios

def update_usuario(id: int, usuario: UsuarioUpdate):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    UPDATE usuarios SET
        nome = %s,
        cpf = %s,
        cep = %s,
        logradouro = %s,
        bairro = %s,
        cidade = %s,
        estado = %s,
        data_atualizacao = CURRENT_TIMESTAMP
    WHERE id = %s
    """
    cursor.execute(query, (
        usuario.nome,
        usuario.cpf,
        usuario.cep,
        usuario.logradouro,
        usuario.bairro,
        usuario.cidade,
        usuario.estado,
        id
    ))
    conn.commit()
    cursor.close()
    conn.close()

def delete_usuario(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
