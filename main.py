from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# criando um instância para Banco de Dados.
db = SQLAlchemy


def create_app():
    application = Flask(__name__)

    # setando as configurações de desenvolvimento
    application.config.from_object("config.DevelopmentConfig")

    from index import index_blueprint

    application.register_blueprint(index_blueprint)

    db.init_app(application)


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port="34444")
