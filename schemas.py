from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nome: str
    cpf: str
    cep: str
    logradouro: str
    bairro: str
    cidade: str
    estado: str

class UsuarioCreate(UsuarioBase):
    pass

class UsuarioUpdate(UsuarioBase):
    pass
