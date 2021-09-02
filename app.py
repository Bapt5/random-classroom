from flask import Flask, render_template, request, redirect, session, url_for
from flask_session import Session
from flask.json import jsonify

app = Flask(__name__)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=3000, debug=True)
