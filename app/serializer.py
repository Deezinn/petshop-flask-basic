from marshmallow import Schema, fields

# Schema para Pet
class PetSchema(Schema):
    id = fields.Int(dump_only=True)
    nome_pet = fields.Str(required=True)
    nome_propietario = fields.Str(required=True)

# Função de configuração do serializador
def configure(app):
    pass  # Sem configurações adicionais, mas você pode incluir se necessário
