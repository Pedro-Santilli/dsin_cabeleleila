from main import app
from flask import render_template,request, redirect, url_for, flash
import pandas as pd

def carregar_df():
    return pd.read_excel("database\\usuariosdb.xlsx")
@app.route("/")
def carregar_login():
    return render_template("login.html")
    
@app.route('/',methods=['POST'])
def login():
    df=carregar_df()
    usuario = request.form['usuario']
    senha = request.form['senha']
    
    user = df[(df['usuario'] == usuario) & (df['senha'] == senha)]
    
    if not user.empty:
        flash("Login bem-sucedido!")
        return redirect(url_for('dashboard'))
    else:
        flash("Nome de usuário ou senha incorretos!")
        return carregar_login()
    
@app.route("/cadastro")    
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastro", methods=['POST'])    
def cadastrar():
    df=carregar_df()
    usuario = request.form['usuario']
    senha = request.form['senha']
    email = request.form['email'] 

    new_user = pd.DataFrame({
        'usuario': [usuario],
        'senha': [senha],
        'email': [email]
    })
    dfs = pd.concat([df, new_user], ignore_index=True)

    dfs.to_excel("database\\usuariosdb.xlsx", index=False)

    flash("Cadastro bem-sucedido! Agora você pode fazer login.")
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    return "Bem-vindo ao painel de controle!"
