from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
from flask.json import jsonify

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
    Organisationclasse = [[ "" for i in range (rangee)] for i in range (colonne)]
    if table == 1:
        for i in range (colonne + colonne-1) :
            if i%2 != 0 :
                Organisationclasse.insert(i, [None for i in range (rangee)])
    if table == 2:
        for i in range (colonne + colonne-1) :
            if i%3 == 0 :
                Organisationclasse.insert(i, [None for i in range (rangee)])
    print (Organisationclasse)
    return ('test')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000, debug=True)
