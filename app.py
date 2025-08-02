from flask import Flask, render_template, request
from ext import db
from modelos.resultado import Resultado

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resultados.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Função de juros compostos
def juros_compostos(c, i, t):
    m = c * (1 + (i / 100))**t
    j = m - c
    return round(m, 2), round(j, 2)

@app.route('/', methods=['GET', 'POST'])
def calcular():
    resultado = None
    if request.method == 'POST':
        capital = float(request.form['capital'].replace(",", "."))
        taxa = float(request.form['taxa'].replace(",", "."))
        tempo = int(request.form['tempo'])
        montante, juros = juros_compostos(capital, taxa, tempo)

        resultado = {
            'montante': montante,
            'juros': juros,
            'capital': capital,
            'taxa': taxa,
            'tempo': tempo
        }

        novo_resultado = Resultado(
            capital=capital,
            taxa=taxa,
            tempo=tempo,
            montante=montante,
            juros=juros
        )
        db.session.add(novo_resultado)
        db.session.commit()

    return render_template('formulario.html', resultado=resultado)

# Banco precisa ser criado uma vez:
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

