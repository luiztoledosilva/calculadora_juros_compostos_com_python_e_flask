from flask import Flask, render_template, request

app = Flask(__name__)

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
    return render_template('formulario.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)