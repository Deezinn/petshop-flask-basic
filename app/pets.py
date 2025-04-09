from flask import Blueprint, request, jsonify
from .model import Pet
from .serializer import PetSchema

bp_pet = Blueprint('pets', __name__)
pet_schema = PetSchema()
pets_schema = PetSchema(many=True)

# Cadastrar um novo pet
@bp_pet.route('/cadastrar-pet', methods=['POST'])
def cadastrar_pet():
    data = request.json
    novo_pet = Pet(**data)

    # Inserir no banco de dados
    from .model import db
    db.session.add(novo_pet)
    db.session.commit()

    return jsonify(pet_schema.dump(novo_pet)), 201

# Mostrar todos os pets
@bp_pet.route('/mostrar-pets', methods=['GET'])
def mostrar_pets():
    pets = Pet.query.all()
    return jsonify(pets_schema.dump(pets)), 200

# Deletar um pet pelo ID
@bp_pet.route('/deletar-pet/<int:id>', methods=['DELETE'])
def deletar_pet(id):
    from .model import db
    pet = Pet.query.get_or_404(id)
    db.session.delete(pet)
    db.session.commit()
    return jsonify({'message': 'Pet deletado com sucesso'}), 200

# Modificar um pet pelo ID
@bp_pet.route('/modificar-pet/<int:id>', methods=['PUT'])
def modificar_pet(id):
    from .model import db
    pet = Pet.query.get_or_404(id)
    data = request.json

    # Atualizando os dados do pet
    for key, value in data.items():
        setattr(pet, key, value)

    db.session.commit()
    return jsonify(pet_schema.dump(pet)), 200
