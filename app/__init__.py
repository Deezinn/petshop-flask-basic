from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db, db  # importa o db aqui
from .serializer import configure as config_ma
import os

def create_app():
    app = Flask(__name__)

    # Caminho relativo
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'pets.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Cria diretório instance se não existir
    os.makedirs(app.instance_path, exist_ok=True)

    config_db(app)
    config_ma(app)

    # Usa o `db` importado do model.py
    Migrate(app, db)

    @app.route("/")
    def index():
        return "André Lindo s2 s2"

    from .pets import bp_pet
    app.register_blueprint(bp_pet)

    return app
