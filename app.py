from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
from flask.json import jsonify
import csv
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('tableRoom.html')

@app.route('/generate', methods=['POST', 'GET'])
def generate():
    table = int(request.form['table'])
    colonne = int(request.form['colonne'])
    rangee = int(request.form['rangee'])
    # roomName = int(request.form['roomName'])
    Organisationclasse = [[ "" if (table == 1 and j%2 == 0) or (table == 2 and (j+1)%3 !=0 ) else None for j in range(colonne * table + (colonne-1))] for i in range(rangee)]
    print (Organisationclasse)
    return ('test')

@app.route('/tableau', methods=['POST'])
def tableau():
    excel = pd.read_excel(request.form[''])
    excel.to_csv(csv)
    with open(request.form[], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row['first_name'], row['last_name'])



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000, debug=True)
