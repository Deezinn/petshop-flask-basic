from app import create_app

app = create_app()

with app.app_context():
    app.db.create_all()
    print("✅ Banco de dados criado com sucesso!")
