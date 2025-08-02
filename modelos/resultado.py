from ext import db

class Resultado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capital = db.Column(db.Float, nullable=False)
    taxa = db.Column(db.Float, nullable=False)
    tempo = db.Column(db.Integer, nullable=False)
    montante = db.Column(db.Float, nullable=False)
    juros = db.Column(db.Float, nullable=False)

