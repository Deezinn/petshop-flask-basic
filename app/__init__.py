from flask import Flask
from flask_migrate import Migrate
from .model import configure as config_db
from .serializer import configure as config_ma

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/pets.db'

    config_db(app)
    config_ma(app)

    Migrate(app, app.db)

    @app.route("/")
    def index():
        return "API Flask está rodando na Azure! 🐍 CRUD de um petshop"

    from .pets import bp_pet
    app.register_blueprint(bp_pet)

    return app
