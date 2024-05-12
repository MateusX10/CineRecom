from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)


class Filme(db.Model):

    __tablename__ = 'filme'

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    titulo = db.Column(db.String)

    sinopse = db.Column(db.String)

    ano_lancamento = db.Column(db.Integer)

    genero = db.Column(db.String)

    average_rate = db.Column(db.Float)

    popularidade = db.Column(db.Integer)

    classificacao = db.Column(db.String)

    duracao = db.Column(db.Float)

    poster = db.Column(db.String) #armazenar o caminho da imagem do filme

    link_trailer = db.Column(db.String)

    diretor = db.Column(db.String)

    elenco = db.Column(db.String)
                              



class Serie(db.Model):

    __tablename__ = 'serie'

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    titulo = db.Column(db.String)

    sinopse = db.Column(db.String)

    ano_lancamento = db.Column(db.Integer)

    genero = db.Column(db.String)

    numero_episodios = db.Column(db.Integer)

    numero_temporadas = db.Column(db.Integer)
 
    average_rate = db.Column(db.Float)

    popularidade = db.Column(db.Integer)

    classificacao = db.Column(db.String)

    duracao = db.Column(db.Float)

    poster = db.Column(db.String) #armazenar o caminho da imagem da série

    link_trailer = db.Column(db.String)

    diretor = db.Column(db.String)

    elenco = db.Column(db.String)



class Comentario(db.Models):


    __tablename__ = 'comentario'

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    comentario = db.Column(db.Text, nullable=False)

    data_comentario = db.Column(db.Date, nullable=False)


class Review(db.Models):

    __tablename_ = 'review'

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    review = db.Column(db.Text)

    data_review = db.Column(db.Date)

    recomendado = db.Column(db.Bool)

    review_rate = db.Column(db.Float)


class Configuracoes:

    __tablename__ = 'cofigurações'

    tema_do_site = db.Column(db.String)




class Usuario(db.Model):

    __tablename__ = 'usuario'

    __id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String, unique=True, nullable=False)

    email = db.Column(db.String, unique=True, nullable=False)

    senha = db.Column(db.String, nullable=False)

    data_nascimento = db.Column(db.Date, nullable=False)

    genero = db.Column(db.String)



class Administrador(Usuario):

    __tablename__ = 'administrador'

    id =  db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key=True)



class Perfil:

    __tablename__ = 'perfil'

    __idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)

    obras_assistidas = db.Column(db.String)

    obras_assistindo = db.Column(db.String)

    obras_a_assistir = db.Column(db.String)

    generos_preferidos = db.Column(db.String)

    obras_preferidas = db.Column(db.String)








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