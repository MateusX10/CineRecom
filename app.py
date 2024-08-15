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

    id_filme = db.Column(db.Integer, db.ForeignKey('filme.id'), nullable=False)

    id_serie = db.Column(db.Integer, db.ForeignKey('serie.id'), nullable=False)

    #cria um atributo "comentarios" na classe Filme
    filme = db.relationship('Filme', backref=db.backref('comentarios', lazy=True))

    # cria um atributo "comentarios" na classe nSerie
    serie = db.relationship('Serie', backref=db.backref('comentarios', lazy=True))


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

    id_filme = db.Column(db.Integer, db.ForeignKey('filme.id'), nullable=False)

    id_serie = db.Column(db.Integer, db.ForeignKey('serie.id'), nullable=False)

    # cria atributo "reviews" na classe "Filme"
    filme = db.relationship('Filme', backref=db.backref('reviews', lazy=True))

    # cria atributo "reviews" na classe "Serie"
    serie = db.relationship('Serie', backref=db.backref('reviews', lazy=True))
    


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
    '''-> Lista os filmes e séries da página inicial.
    '''


    filmes = Filme.query.all()

    series = Serie.query.all()

    return render_template('index.html', filmes=filmes, series=series)



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


    usuario_pesquisou_por_outro_usuario = request.args.get('pesquisa_por_usuario')

    if usuario_pesquisou_por_outro_usuario:
        usuario = usuario_pesquisou_por_outro_usuario
        usuarios = Usuario.query.filter(Usuario.username.contains(usuario)).all()

    else:

        usuarios = Usuario.query.all()


    return render_template("usuarios/listar.html", usuarios=usuarios)



@app.route('/usuarios/excluir/<int:id>', methods=["POST"])
def excluir_usuario(id):

    # estou pegando o usuário com id "x" .Estou pegando a primeira consulta que der match
    usuario_a_ser_excluido = Usuario.query.filter_by(id=id).first()

    if usuario_a_ser_excluido:

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


@app.route('/usuarios/perfil/<username>')
def perfil_usuario(username):

    usuario = Usuario.query.filter_by(username=username).first()

    return render_template("perfil/index.html", usuario=usuario)



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

    usuario_pesquisou_por_administrador = request.args.get('pesquisa_por_administrador')

    if usuario_pesquisou_por_administrador:
        administrador = usuario_pesquisou_por_administrador
        administradores = Administrador.query.filter(Administrador.username.contains(administrador)).all()

    else:

        administradores = Administrador.query.all()


    return render_template("administradores/listar.html", administradores=administradores)



@app.route('/administradores/excluir/<int:id>', methods=["POST"])
def excluir_administrador(id):

    # estou pegando o administrador com id "x" .Estou pegando a primeira consulta que der match
    administrador_a_ser_excluido = Administrador.query.filter_by(id=id).first()

    if administrador_a_ser_excluido:

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


@app.route('/administradores/perfil/<username>')
def perfil_administrador(username):

    administrador = Administrador.query.filter_by(username=username).first()

    return render_template("perfil/index.html", usuario=administrador)




@app.route('/filmes')
def filmes():
    return render_template("filmes/index.html")


@app.route('/cadastrar_filme')
def cadastrar_filme():

    return render_template("filmes/cadastro.html")


@app.route("/filmes/cadastro", methods=["GET", "POST"])
def cadastro_filmes():

    import os

    
    if request.method == "POST":
        titulo = request.form.get("titulo")
        sinopse = request.form.get("sinopse")
        ano_lancamento = int(request.form.get("ano_lancamento"))  # Convertendo para inteiro
        genero = request.form.get("genero")
        average_rate = request.form.get("average_rate")
        popularidade = request.form.get("popularidade")
        classificacao = request.form.get("classificacao")
        duracao = request.form.get("duracao")
        poster = request.form.get("poster")
        link_trailer = request.form.get("link_trailer")
        diretores = request.form.get("diretores")
        elenco = request.form.get("elenco")

        if titulo and sinopse and ano_lancamento and genero and average_rate and popularidade and classificacao and duracao and poster and link_trailer and diretores and elenco:

            #dados_do_poster = arquivo_do_poster.read()

            #caminho_da_imagem = "/home/mateus/Documentos/estudos/faculdade/tcc/imagens"


            filme1 = Filme(titulo, sinopse, ano_lancamento, genero, average_rate, popularidade, classificacao, duracao, poster,  link_trailer, diretores, elenco)
            db.session.add(filme1)
            db.session.commit()
            return redirect(url_for("filmes"))

@app.route('/filmes/listar')
def listar_filmes():

    usuario_pesquisou_por_titulo_de_obra = request.args.get('pesquisa_por_titulo')

    if usuario_pesquisou_por_titulo_de_obra:
        filme = usuario_pesquisou_por_titulo_de_obra
        filmes = Filme.query.filter(Filme.titulo.contains(filme)).all()

    else:
    
        filmes = Filme.query.all()

    return render_template("filmes/listar.html", filmes=filmes)


@app.route('/filme/<int:id>')
def pagina_filme(id):


    filme = Filme.query.filter_by(id=id).first()


    return render_template("filmes/pagina-filme.html", filme=filme)


@app.route('/filme/atualizar/<int:id>', methods=["POST", "GET"])
def atualizar_filme(id):
    filme = Filme.query.filter_by(id=id).first()

    if request.method == "POST":
        titulo = request.form.get("titulo")
        sinopse = request.form.get("sinopse")
        ano_lancamento = request.form.get("ano_lancamento")
        genero = request.form.get("genero")
        average_rate = request.form.get("average_rate")
        popularidade = request.form.get("popularidade")
        classificacao = request.form.get("classificacao")
        duracao = request.form.get("duracao")
        poster = request.form.get("poster")
        link_trailer = request.form.get("link_trailer")
        diretores = request.form.get("diretores")
        elenco = request.form.get("elenco")

        if titulo and sinopse and ano_lancamento and genero and average_rate and popularidade and classificacao and duracao and poster and link_trailer and diretores and elenco:
            filme.titulo = titulo
            filme.sinopse = sinopse
            filme.ano_lancamento = ano_lancamento
            filme.genero = genero
            filme.average_rate = average_rate
            filme.popularidade = popularidade
            filme.classificacao = classificacao
            filme.duracao = duracao
            filme.poster = poster
            filme.link_trailer = link_trailer
            filme.diretores = diretores
            filme.elenco = elenco

            db.session.commit()
            return redirect(url_for("filmes"))  

    return render_template("filmes/atualizar.html", filme=filme)




@app.route("/filme/excluir/<int:id>", methods=["POST"])
def excluir_filme(id):

    filme_a_ser_excluido = Filme.query.filter_by(id=id).first()

    if filme_a_ser_excluido:
        db.session.delete(filme_a_ser_excluido)

    db.session.commit()

    filmes = Filme.query.all()

    return render_template("filmes/listar.html", filmes=filmes)



@app.route('/comentario_cadastrado')
def comentario_cadastrado():

    if request.method == "POST":

        comentario = request.form.get('comentario')

        




@app.route('/series')
def series():

    return render_template("series/index.html")



@app.route('/cadastrar_serie')
def cadastrar_serie():

    return render_template("series/cadastro.html")


@app.route("/seres/cadastro", methods=["GET", "POST"])
def cadastro_series():

    import os

    
    if request.method == "POST":
        titulo = request.form.get("titulo")
        sinopse = request.form.get("sinopse")
        ano_lancamento = int(request.form.get("ano_lancamento"))  # Convertendo para inteiro
        genero = request.form.get("genero")
        numero_episodios = request.form.get("numero_episodios")
        numero_temporadas = request.form.get("numero_temporadas")
        average_rate = request.form.get("average_rate")
        popularidade = request.form.get("popularidade")
        classificacao = request.form.get("classificacao")
        duracao = request.form.get("duracao")
        poster = request.form.get("poster")
        link_trailer = request.form.get("link_trailer")
        diretores = request.form.get("diretores")
        elenco = request.form.get("elenco")

        if titulo and sinopse and ano_lancamento and genero and numero_episodios and numero_temporadas and average_rate and popularidade and classificacao and duracao and poster and link_trailer and diretores and elenco:

            #dados_do_poster = arquivo_do_poster.read()

            #caminho_da_imagem = "/home/mateus/Documentos/estudos/faculdade/tcc/imagens"


            serie1 = Serie(titulo, sinopse, ano_lancamento, genero, numero_episodios, numero_temporadas, average_rate, popularidade, classificacao, duracao, poster,  link_trailer, diretores, elenco)
            db.session.add(serie1)
            db.session.commit()
            return redirect(url_for("series"))

@app.route('/series/listar')
def listar_series():

    usuario_pesquisou_por_titulo_de_obra = request.args.get('pesquisa_por_titulo')

    if usuario_pesquisou_por_titulo_de_obra:
        serie = usuario_pesquisou_por_titulo_de_obra
        series = Serie.query.filter(Serie.titulo.contains(serie)).all()

    else:    

        series = Serie.query.all()


    return render_template("series/listar.html", series=series)


@app.route('/serie/<int:id>')
def pagina_serie(id):


    serie = Serie.query.filter_by(id=id).first()


    return render_template("series/pagina-serie.html", serie=serie)


@app.route('/serie/atualizar/<int:id>', methods=["POST", "GET"])
def atualizar_serie(id):
    serie = Serie.query.filter_by(id=id).first()

    if request.method == "POST":
        titulo = request.form.get("titulo")
        sinopse = request.form.get("sinopse")
        ano_lancamento = request.form.get("ano_lancamento")
        genero = request.form.get("genero")
        numero_episodios = request.form.get("numero_episodios")
        numero_temporadas = request.form.get("numero_temporadas")
        average_rate = request.form.get("average_rate")
        popularidade = request.form.get("popularidade")
        classificacao = request.form.get("classificacao")
        duracao = request.form.get("duracao")
        poster = request.form.get("poster")
        link_trailer = request.form.get("link_trailer")
        diretores = request.form.get("diretores")
        elenco = request.form.get("elenco")

        if titulo and sinopse and ano_lancamento and genero and numero_episodios and numero_temporadas and average_rate and popularidade and classificacao and duracao and poster and link_trailer and diretores and elenco:
            serie.titulo = titulo
            serie.sinopse = sinopse
            serie.ano_lancamento = ano_lancamento
            serie.genero = genero
            serie.average_rate = average_rate
            serie.popularidade = popularidade
            serie.classificacao = classificacao
            serie.duracao = duracao
            serie.poster = poster
            serie.link_trailer = link_trailer
            serie.diretores = diretores
            serie.elenco = elenco

            db.session.commit()
            return redirect(url_for("series"))  

    return render_template("series/atualizar.html", serie=serie)




@app.route("/serie/excluir/<int:id>", methods=["POST"])
def excluir_serie(id):

    serie_a_ser_excluido = Serie.query.filter_by(id=id).first()


    if serie_a_ser_excluido:


        db.session.delete(serie_a_ser_excluido)

    db.session.commit()

    series = Serie.query.all()

    return render_template("series/listar.html", series=series)



@app.route('/configuracoes')
def configuracoes():

    return render_template("configuracoes/index.html")


@app.route('/listar_obras')
def listar_obras():
    '''-> função exclusiva para receber as pesquisas por obras feitas na tela inicial do sistema.
    '''

    obra = request.args.get('pesquisa_por_titulo')

    if obra:

        filmes = Filme.query.filter(Filme.titulo.contains(obra))

        series = Serie.query.filter(Serie.titulo.contains(obra))

    else:

        filmes = Filme.query.all()

        series = Serie.query.all()

    return render_template("index.html", filmes=filmes, series=series)



if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)





