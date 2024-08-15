from flask import Flask, render_template, request, redirect

app = Flask(__name__)

musica = []
favorito = False

@app.route('/')
def index():
    print(f"Músicas na página inicial: {musica}")  # Print de depuração
    return render_template('index.html', musica=musica)

@app.route('/adicionar_musica', methods=['GET', 'POST'])
def adicionar_musica():
    """
    Rota para adicionar um novo filme.
    Se o método for POST, adiciona o novo filme à lista.
    Se não, exibe o formulário para adicionar um novo filme.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        artista = request.form['nome']
        favorito = request.form.get('favorito', 'off') == 'on'
        codigo = len(musica)
        musica.append([codigo, nome, telefone, artista, favorito])
        print(f"Música adicionado: {musica[-1]}")  # Print de depuração
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        return render_template('adicionar_musica.html')  # Renderiza o formulário de adicionar filme

@app.route('/editar_musica/<int:codigo>', methods=['GET', 'POST'])
def editar_musica(codigo):
    """
    Rota para editar um filme existente.
    Se o método for POST, atualiza os detalhes do filme com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do filme para edição.
    """
    global musica  # Indica que a variável 'musica' é global
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        artista = request.form['nome']
        favorito = request.form.get('favorito', 'off') == 'on'
        musica[codigo] = [codigo, nome, telefone, artista, favorito]
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        musica = musica[codigo]
        return render_template('editar_musica.html', musica=musica)  # Renderiza o formulário de edição

@app.route('/apagar_musica/<int:codigo>')
def apagar_musica(codigo):
    """
    Rota para apagar um contato da lista.
    """
    del musica[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial

if __name__=='__main__':
    app.run(debug=True)