from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)



@app.route('/')
def index():

    return "Página home"    


@app.route('/filmes')
def filmes():

    return "página filmes"


@app.route('/series')
def series():

    return "página séries"


@app.route('/usuarios')
def usuarios():

    return "página usuários"

@app.route('/administradores')
def administradores():

    return "página administradores"


@app.route('/perfil')
def perfil():
    return "perfil de @username"


@app.route('/configuracoes')
def configuracoes():

    return 'configurações do sistema'



if __name__ == '__main__':

    app.run(debug=True)