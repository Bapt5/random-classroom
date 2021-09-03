from flask import Flask, render_template, request, redirect, session, url_for
from flask.json import jsonify
import csv
import pandas as pd

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
    Organisationclasse = [[ "" if (table == 1 and j%2 == 0) or (table == 2 and (j+1)%3 !=0 ) else None for j in range(colonne * table + (colonne-1))] for i in range(rangee)]
    session['currentRoom'] = Organisationclasse
    return redirect(url_for('enterStudent'))


@app.route('/enterStudent', methods=['GET'])
def enterStudent():
    return render_template('enterStudent.html')


@app.route('/tableau', methods=['POST'])
def tableau():
    file = request.files['eleves']
    ext = getExtension(file)
    if ext == 'xls' or ext == 'xlsx':
        excel = pd.read_excel(file)
        excel.to_csv('listeEleve.csv')
        with open('listeEleve.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
    elif ext == 'csv':
        reader = csv.DictReader(file.read())
    # for row in reader:
    #     print("row")
    return ('test')



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000, debug=True)
