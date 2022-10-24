from main import db


class Usuario(db):
    __tablename__ = "usuario"
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    senha = db.Column(db.String(150), nullable=False)
    permissao = db.Column(db.String(150), nullable=False)
    telefone = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.String(150), nullable=False)


class Produto(db):
    __tablename__ = "produto"
    id_produto = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float, nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    imagem = db.Column(db.String(150), nullable=True)