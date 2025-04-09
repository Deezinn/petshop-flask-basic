from flask_sqlalchemy import SQLAlchemy

# Instanciando o SQLAlchemy
db = SQLAlchemy()

# Modelo Pet
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_pet = db.Column(db.String(80), nullable=False)
    nome_propietario = db.Column(db.String(80), nullable=False)

# Função de configuração do banco de dados
def configure(app):
    db.init_app(app)
