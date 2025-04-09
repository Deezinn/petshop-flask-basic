from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma
import os

def create_app():
    app = Flask(__name__)

    # Usar a variável de ambiente ou um caminho relativo para o banco de dados SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.getenv('DATABASE_URL', 'instance/pets.db')}"

    # Configurações do banco de dados e serializador
    config_db(app)
    config_ma(app)

    # Migrate
    Migrate(app, app.db)

    @app.route("/")
    def index():
        return "André Lindo s2 s2"

    # Registrando o blueprint de pets
    from .pets import bp_pet
    app.register_blueprint(bp_pet)

    return app
