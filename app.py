from flask import Flask, render_template, request, redirect, session, url_for
from flask.json import jsonify
import csv
import os
import json
from random import choice

app = Flask(__name__)

def getExtension(file):
    return file.filename.split('.')[-1]

@app.route('/')
def index():
    return render_template('tableRoom.html')


@app.route('/generate', methods=['POST'])
def generate():
    table = int(request.form['table'])
    colonne = int(request.form['colonne'])
    rangee = int(request.form['rangee'])
    # roomName = int(request.form['roomName'])
    organisationClasse = [[ "" if (table == 1 and j%2 == 0) or (table == 2 and (j+1)%3 !=0 ) else None for j in range(colonne * table + (colonne-1))] for i in range(rangee)]
    if 'jquery' in request.form:
        return render_template('generateClass.html', classe=organisationClasse)
    else:
        session['currentRoom'] = organisationClasse
        return redirect(url_for('enterStudent'))


@app.route('/enterStudent', methods=['GET'])
def enterStudent():
    if 'currentRoom' in session:
        return render_template('enterStudent.html', classe=session['currentRoom'])
    else:
        return redirect(url_for('index'))


@app.route('/tableau', methods=['POST'])
def tableau():
    if 'eleves' in request.files:
        file = request.files['eleves']
        file.save(file.filename)
        with open (file.filename,'r', encoding='utf-8') as f :
            reader = csv.DictReader(f, delimiter=';')
            eleves = [row['\ufeffÉlève'] for row in reader]
        os.remove(file.filename)
        session['currentListe'] = eleves
        return redirect(url_for('plan'))
    else:
        return redirect(url_for('enterStudent'))

@app.route('/plan')
def plan():
    if 'currentListe' in session:
        plan = session['currentRoom'].copy()
        liste = session['currentListe'].copy()
        for i, row in enumerate(plan):
            for j, col in enumerate(row):
                if col != None:
                    if len(liste)>0:
                        choix = choice(liste)
                        plan[i][j] = choix
                        liste.remove(choix)
                    else:
                        break
        return render_template('plan.html', classe=plan)
    else:
        return redirect(url_for('enterStudent'))


if __name__ == '__main__':
    app.secret_key = os.urandom(24)
    app.run(host="127.0.0.1", port=3000, debug=True)
