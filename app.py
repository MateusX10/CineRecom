from flask import Flask


app = Flask(__name__)



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