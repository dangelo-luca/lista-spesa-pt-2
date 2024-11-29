from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, ListaSpesa

#inizializza l'app Flask
app = Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lista_spesa.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

lista_spesa = ["pippo"]

@app.route('/')
def home():
    lista_spesa = ListaSpesa.query.all()
    return render_template('index.html',lista=lista_spesa)

@app.route('/aggiungi', methods=['POST'])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        nuovo_elemento = ListaSpesa(elemento=elemento) #aggiunge un nuovo elemento alla lista spesa ovvero viene creata una nuova riga nella tabella del Database
        db.session.add(nuovo_elemento) #in questa riga di codice vengono memorizzati tutti i dati che devono essere aggiunti al Database
        db.session.commit() #serve per salvare delle modifiche nel Database in questo caso aggiunge l'elemento appena inserito nel Database
    return redirect(url_for('home'))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    elemento = ListaSpesa.query.get(indice) #cerca, tramite l'indice di recuperare una riga dal Database
    db.session.delete(elemento) #questa riga permette di eliminare un elemento dal Database
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/svuota', methods = ['POST'])
def svuota():
    ListaSpesa.query.delete() #permette di cancellare tutte le righe del Database
    db.session.commit()
    return redirect(url_for('home'))

#avvio dell'app Flask
if __name__ == '__main__':
    app.run(debug=True)