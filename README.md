# README - API de Usuários

## Descrição da Aplicação

A API de Usuários é um projeto desenvolvido em Python utilizando o framework Flask. Esta API permite gerenciar informações de usuários, possibilitando a criação, leitura, atualização e exclusão (CRUD) de dados.

Os dados dos usuários incluem informações pessoais (como nome, CPF) e endereço (CEP, logradouro, bairro, cidade, estado). A aplicação agora utiliza um sistema de preenchimento automático para o endereço com base no CEP, onde, ao digitar o CEP, os campos de logradouro, bairro, cidade e estado são automaticamente preenchidos, sem sobrescrever os dados já preenchidos.

A aplicação utiliza validação de dados com **Pydantic** para garantir a consistência dos dados enviados.

## Requisitos

- Python 3.10 ou superior
- Gerenciador de pacotes pip
- Virtualenv (opcional, mas recomendado)

## Instalação

1. Clone o repositório

```bash
git clone https://github.com/usuario/api_usuarios.git
cd api_usuarios
Crie e ative um ambiente virtual
bash
Copy code
python -m venv myenv
source myenv/bin/activate  # No Windows: myenv\Scripts\activate
Instale as dependências
bash
Copy code
pip install -r requirements.txt
Como Rodar a Aplicação
Execute o servidor Flask

bash
Copy code
flask run
Por padrão, o servidor rodará em http://127.0.0.1:5000.

Testando a API
Você pode utilizar ferramentas como Postman, Insomnia ou curl para testar os endpoints.

Endpoints da API
1. Criar Usuário
Descrição: Adiciona um novo usuário.
Método: POST
Endpoint: /usuarios
Exemplo de Corpo da Requisição:

json
Copy code
{
    "nome": "Sarah Ribeiro",
    "cpf": "12345678902",
    "cep": "12345678",
    "logradouro": "Rua Exemplo",
    "bairro": "Bairro Exemplo",
    "cidade": "Cidade Exemplo",
    "estado": "SP"
}
Resposta de Sucesso (201):

json
Copy code
{
    "message": "Usuário criado com sucesso"
}
2. Listar Usuários
Descrição: Retorna todos os usuários cadastrados.
Método: GET
Endpoint: /usuarios
Resposta de Sucesso (200):

json
Copy code
[
    {
        "id": 1,
        "nome": "Sarah Ribeiro",
        "cpf": "12345678902",
        "cep": "12345678",
        "logradouro": "Rua Exemplo",
        "bairro": "Bairro Exemplo",
        "cidade": "Cidade Exemplo",
        "estado": "SP"
    }
]
3. Atualizar Usuário
Descrição: Atualiza as informações de um usuário específico.
Método: PUT
Endpoint: /usuarios/<id>
Exemplo de Corpo da Requisição:

json
Copy code
{
    "nome": "Sarah Ribeiro",
    "cpf": "12345678902",
    "cep": "12345678",
    "logradouro": "Rua Zeli Maciel",
    "bairro": "Paciência",
    "cidade": "Rio de Janeiro",
    "estado": "RJ"
}
Resposta de Sucesso (200):

json
Copy code
{
    "message": "Usuário atualizado com sucesso"
}
4. Deletar Usuário
Descrição: Remove um usuário do sistema.
Método: DELETE
Endpoint: /usuarios/<id>
Resposta de Sucesso (200):

json
Copy code
{
    "message": "Usuário deletado com sucesso"
}
Estrutura do Projeto
bash
Copy code
api_usuarios/
├── app.py               # Arquivo principal com a lógica da API
├── models.py            # Modelos do Pydantic para validação de dados
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
Validações
A API utiliza Pydantic para garantir que os dados enviados no corpo das requisições atendam os critérios definidos, como:

CPF deve ser válido.
Campos obrigatórios, como nome, cep, etc., devem estar presentes (a menos que definidos como opcionais).
Além disso, foi implementada uma funcionalidade de preenchimento automático de endereço. Ao digitar o CEP, os campos de logradouro, bairro, cidade e estado serão automaticamente preenchidos, sem sobrescrever dados já existentes no formulário.

Como Personalizar
Adicionar novos campos: Modifique o arquivo models.py para incluir novos atributos no modelo.
Integrar um banco de dados: Substitua o armazenamento atual por uma integração com bancos de dados como SQLite, PostgreSQL, ou MongoDB.
Melhorar a segurança: Adicione autenticação e autorização usando bibliotecas como Flask-JWT-Extended.
Possíveis Erros e Soluções
Erro 422 - Validation Error: Verifique se todos os campos obrigatórios foram enviados corretamente.
Erro 404 - Usuário não encontrado: Certifique-se de usar um ID válido ao buscar, atualizar ou deletar um usuário.# api_usuarios
# api_usuarios
