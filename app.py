from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from schemas import UsuarioCreate, UsuarioUpdate
from crud import create_usuario, get_usuarios, update_usuario, delete_usuario

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route('/usuarios', methods=['POST'])
def create():
    data = request.get_json()
    usuario = UsuarioCreate(**data)
    create_usuario(usuario)
    return jsonify({"message": "Usuário criado com sucesso!"}), 201

@app.route('/usuarios', methods=['GET'])
def read():
    usuarios = get_usuarios()
    return jsonify(usuarios), 200

@app.route('/usuarios/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    usuario = UsuarioUpdate(**data)
    update_usuario(id, usuario)
    return jsonify({"message": "Usuário atualizado com sucesso!"}), 200

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete(id):
    delete_usuario(id)
    return jsonify({"message": "Usuário excluído com sucesso!"}), 200

@app.route('/endereco/<cep>', methods=['GET'])
def get_endereco(cep):
    try:
        response = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
        data = response.json()

        if "erro" in data:
            return jsonify({"error": "CEP não encontrado"}), 404
        
        return jsonify({
            "logradouro": data.get("logradouro", ""),
            "bairro": data.get("bairro", ""),
            "cidade": data.get("localidade", ""),
            "estado": data.get("uf", ""),
        })

    except Exception as e:
        return jsonify({"error": f"Erro ao buscar CEP: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
