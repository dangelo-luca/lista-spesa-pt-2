from flask import Flask, render_template, request, redirect, url_for
#inizializza l'app Flask

app = Flask(__name__)

lista_spesa = ["pippo"]

#rotta principale
@app.route('/')
def home():

    return render_template('index.html')
#avvio dell'app Flask

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista_spesa.append(elemento)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)