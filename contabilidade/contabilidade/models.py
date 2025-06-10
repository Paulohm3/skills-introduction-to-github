from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Conta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)  # Ativo, Passivo, Receita, Despesa

class Lancamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conta_debito = db.Column(db.String(100), nullable=False)
    conta_credito = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Float, nullable=False)
