from flask_marshmallow import Marshmallow
from .model import Pet

ma = Marshmallow()

def configure(app):
    ma.init_app(app)

class PetSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pet
        load_instance = True  
