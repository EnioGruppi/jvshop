from flask import Flask, request, render_template, session, redirect
from contextlib import closing
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html', mensagem = '')

@app.route('/saias')
def skirts():
    return render_template('saias.html', mensagem = '')

@app.route('/vestidos')
def dresses():
    return render_template('vestidos.html', mensagem = '')

@app.route('/croppeds')
def croppeds():
    return render_template('croppeds.html', mensagem = '')

@app.route('/acessorios')
def accessories():
    return render_template('acessorios.html', mensagem = '')

@app.route('/calcas')
def calcas():
    return render_template('calcas.html', mensagem = '')


if __name__ == '__main__':
    app.run(debug=True)