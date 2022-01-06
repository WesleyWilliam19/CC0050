from database import db

class Usuario(db.Model):
    id = db.Column (db.Integer, primary_key=True)
    nome = db.Column (db.String(200), unique=False, nullable=False) #unique = nome unico (False = permite nomes iguais)
    username = db.Column (db.String(80), unique=True, nullable=False) # (True = unico, não permite outros iguais)
    email = db.Column(db.String(120), unique=True, nullable=True) # nullable=True (a linha pode ser nulo)    
    telefone = db.Column(db.String(20), unique=False, nullable=True)
    senha = db.Column(db.String(80), unique=False, nullable=False)
    emprestimos = db.relationship('Emprestimo',backref='usuario',lazy=True)

