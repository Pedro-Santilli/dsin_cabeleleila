from flask import Flask

app = Flask(__name__)
app.secret_key = 'chavesecreta'

from rotas import *

if __name__=="__main__":
    app.run()