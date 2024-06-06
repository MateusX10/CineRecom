from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)


class Filme(db.Model):

    __tablename__ = 'filme'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

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


    def __init__(self, titulo, sinopse, ano_lancamento, genero, average_rate, popularidade, classificacao, duracao, poster, link_trailer, diretor, elenco):

        self.titulo = titulo

        self.sinopse = sinopse

        self.ano_lancamento = ano_lancamento

        self.genero = genero

        self.average_rate = average_rate

        self.popularidade = popularidade

        self.classificacao = classificacao

        self.duracao = duracao

        self.poster = poster

        self.link_trailer = link_trailer

        self.diretor = diretor

        self.elenco = elenco
                              



class Serie(db.Model):

    __tablename__ = 'serie'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

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



    def __init__(self, titulo, sinopse, ano_lancamento, genero, numero_episodios, numero_temporadas, average_rate, popularidade, classificacao, duracao, poster, link_trailer, diretor, elenco):

        self.titulo = titulo

        self.sinopse = sinopse

        self.ano_lancamento = ano_lancamento

        self.genero = genero

        self.numero_episodios = numero_episodios

        self.numero_temporadas = numero_temporadas

        self.average_rate = average_rate

        self.popularidade = popularidade

        self.classificacao = classificacao

        self.duracao = duracao

        self.poster = poster

        self.link_trailer = link_trailer

        self.diretor = diretor

        self.elenco = elenco
                              





class Comentario(db.Model):


    __tablename__ = 'comentario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    comentario = db.Column(db.Text, nullable=False)

    data_comentario = db.Column(db.Date, nullable=False)


    def __init__(self, comentario, data_comentario):

        self.comentario = comentario


        self.data_comentario = data_comentario


class Review(db.Model):

    __tablename_ = 'review'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    review = db.Column(db.Text)

    data_review = db.Column(db.Date)

    recomendado = db.Column(db.Boolean)

    review_rate = db.Column(db.Float)


    def __init__(self, review, data_review, recomendado, review_rate):

        self.review = review

        self.data_review = data_review

        self.recomendado = recomendado

        self.review_rate = review_rate


class Configuracoes:

    __tablename__ = 'cofigurações'

    tema_do_site = db.Column(db.String)


    def __init__(self, tema_do_site):

        self.tema_do_site = tema_do_site




class Usuario(db.Model):

    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String, unique=True, nullable=False)

    email = db.Column(db.String, unique=True, nullable=False)

    senha = db.Column(db.String, nullable=False)

    data_nascimento = db.Column(db.Date, nullable=False)

    genero = db.Column(db.String)


    def __init__(self, username, email, senha, data_nascimento, genero):

        self.username = username

        self.email = email

        self.senha = senha


        self.data_nascimento = data_nascimento

        self.genero = genero



class Administrador(db.Model): # usuário
 
    __tablename__ = 'administrador'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String, unique=True, nullable=False)

    email = db.Column(db.String, unique=True, nullable=False)

    senha = db.Column(db.String, nullable=False)

    data_nascimento = db.Column(db.Date, nullable=False)

    genero = db.Column(db.String)


    def __init__(self, username, email, senha, data_nascimento, genero):

        self.username = username

        self.email = email

        self.senha = senha


        self.data_nascimento = data_nascimento

        self.genero = genero



class Perfil(db.Model):

    __tablename__ = 'perfil'

    idUsuario = db.Column(db.Integer, primary_key=True, autoincrement=True)

    obras_assistidas = db.Column(db.String)

    obras_assistindo = db.Column(db.String)

    obras_a_assistir = db.Column(db.String)

    generos_preferidos = db.Column(db.String)

    obras_preferidas = db.Column(db.String)


    def __init__(self, obras_assistidas, obras_assistindo, obras_a_assistir, generos_preferidos, obras_preferidas):

        self.obras_assistidas = obras_assistidas

        self.obras_assistindo = obras_assistindo

        self.obras_a_assistir = obras_a_assistir

        self.generos_preferidos = generos_preferidos

        self.obras_preferidas = obras_preferidas





@app.route('/')
def index():

    return render_template('index.html')



@app.route('/usuarios')
def usuarios():

    return render_template('usuarios/index.html')

@app.route('/usuarios/cadastrar')
def cadastrar_usuario():

    return render_template("usuarios/cadastro.html")


@app.route('/usuarios/cadastro', methods=["GET", "POST"])
def cadastro_usuario():


    import datetime

    if request.method == "POST":

        username = request.form.get("username")

        email = request.form.get('email')

        senha = request.form.get("senha")

        data_de_nascimento = request.form.get('data de nascimento')

        
        

        genero = request.form.get('gênero')

        if username and email and senha and data_de_nascimento and genero:


            data_de_nascimento = datetime.datetime.strptime(data_de_nascimento, '%Y-%m-%d').date()


            usuario1 = Usuario(username, email, senha, data_de_nascimento, genero)

            # adiciona objeto ao banco de dados
            db.session.add(usuario1) 

            # adiciona efetivamente o usuário ao banco de dados
            db.session.commit()

        return redirect(url_for('usuarios'))


@app.route('/usuarios/lista_usuarios')
def listar_usuarios():

    usuarios = Usuario.query.all()


    return render_template("usuarios/listar.html", usuarios=usuarios)



@app.route('/usuarios/excluir/<int:id>')
def excluir_usuario(id):

    # estou pegando o usuário com id "x" .Estou pegando a primeira consulta que der match
    usuario_a_ser_excluido = Usuario.query.filter_by(id=id).first()


    db.session.delete(usuario_a_ser_excluido)

    db.session.commit()

    usuarios = Usuario.query.all()


    return render_template("usuarios/listar.html", usuarios=usuarios)



@app.route('/usuarios/atualizar/<int:id>', methods=["GET", "POST"])
def atualizar_usuario(id):


    import datetime

    usuario =    Usuario.query.filter_by(id=id).first()

    if request.method == "POST":

        username = request.form.get("username")

        email = request.form.get("email")

        senha = request.form.get("senha")

        data_de_nascimento = request.form.get("data de nascimento")

        genero = request.form.get("gênero")

        if username and email and senha and data_de_nascimento and genero:

            data_de_nascimento = datetime.datetime.strptime(data_de_nascimento, '%Y-%m-%d').date()

            usuario.username = username

            usuario.email = email

            usuario.senha = senha

            usuario.data_nascimento = data_de_nascimento

            usuario.genero = genero

            db.session.commit()

            return redirect(url_for("listar_usuarios"))


    return render_template("usuarios/atualizar.html", usuario=usuario)



@app.route("/administradores")
def administradores():

    return render_template("administradores/index.html")





@app.route('/administradores/cadastrar')
def cadastrar_administrador():

    return render_template("administradores/cadastro.html")


@app.route('/administradores/cadastro', methods=["GET", "POST"])
def cadastro_administrador():


    import datetime

    if request.method == "POST":

        username = request.form.get("username")

        email = request.form.get('email')

        senha = request.form.get("senha")

        data_de_nascimento = request.form.get('data de nascimento')

        
        

        genero = request.form.get('gênero')

        if username and email and senha and data_de_nascimento and genero:


            data_de_nascimento = datetime.datetime.strptime(data_de_nascimento, '%Y-%m-%d').date()


            administrador1 = Administrador(username, email, senha, data_de_nascimento, genero)

            # adiciona objeto ao banco de dados
            db.session.add(administrador1) 

            # adiciona efetivamente o usuário ao banco de dados
            db.session.commit()

        return redirect(url_for('administradores'))


@app.route('/administradores/lista_administradores')
def listar_administradores():

    administradores = Administrador.query.all()


    return render_template("administradores/listar.html", administradores=administradores)



@app.route('/administradores/excluir/<int:id>')
def excluir_administrador(id):

    # estou pegando o administrador com id "x" .Estou pegando a primeira consulta que der match
    administrador_a_ser_excluido = Administrador.query.filter_by(id=id).first()


    db.session.delete(administrador_a_ser_excluido)

    db.session.commit()

    administradores = Administrador.query.all()


    return render_template("administradores/listar.html", administradores=administradores)



@app.route('/administradores/atualizar/<int:id>', methods=["GET", "POST"])
def atualizar_administrador(id):


    import datetime

    administrador = Administrador.query.filter_by(id=id).first()

    if request.method == "POST":

        username = request.form.get("username")

        email = request.form.get("email")

        senha = request.form.get("senha")

        data_de_nascimento = request.form.get("data de nascimento")

        genero = request.form.get("gênero")

        if username and email and senha and data_de_nascimento and genero:

            data_de_nascimento = datetime.datetime.strptime(data_de_nascimento, '%Y-%m-%d').date()

            administrador.username = username

            administrador.email = email

            administrador.senha = senha

            administrador.data_nascimento = data_de_nascimento

            administrador.genero = genero

            db.session.commit()

            return redirect(url_for("listar_administradores"))


    return render_template("administradores/atualizar.html", administrador=administrador)




@app.route('/filmes')
def filmes():

    return render_template("filmes/index.html")


@app.route('/cadastrar_filme')
def cadastrar_filme():

    return render_template("filmes/cadastro.html")


@app.route("/listar_filmes")
def listar_filmes():

    pass






@app.route('/series')
def series():

    return "página séries"








@app.route('/usuarios/perfil/<username>')
def perfil_usuario(username):

    usuario = Usuario.query.filter_by(username=username).first()

    return render_template("perfil/index.html", usuario=usuario)


@app.route('/administradores/perfil/<username>')
def perfil_administrador(username):

    administrador = Administrador.query.filter_by(username=username).first()

    return render_template("perfil/index.html", usuario=administrador)


@app.route('/configuracoes')
def configuracoes():

    return render_template("configuracoes/index.html")



if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(debug=True)





