from flask import Flask, render_template, request, redirect

app = Flask(__name__)

musica = []
favorito = False #Retirado do antigo código

@app.route('/')
def index():
    print(f"Músicas na página inicial: {musica}")  # Print de depuração
    return render_template('index.html', musica=musica)

@app.route('/adicionar_musica', methods=['GET', 'POST'])
def adicionar_musica():

    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        artista = request.form['nome']
        favorito = request.form.get('favorito', 'off') == 'on'
        codigo = len(musica)
        musica.append([codigo, nome, telefone, artista, favorito])
        print(f"Música adicionado: {musica[-1]}")
        # Depuração, ela exibe no console (ou terminal) uma mensagem
        # indicando qual música foi recentemente adicionada à lista musica.

        return redirect('/')
    else:
        return render_template('adicionar_musica.html')

@app.route('/editar_musica/<int:codigo>', methods=['GET', 'POST'])
def editar_musica(codigo):
    # GET:Preenche o formulário de edição com os dados da música existente.

    global musica
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        artista = request.form['nome']
        favorito = request.form.get('favorito', 'off') == 'on'
        musica[codigo] = [codigo, nome, telefone, artista, favorito]
        return redirect('/')
    else:
        musica = musica[codigo]
        return render_template('editar_musica.html', musica=musica)  # Renderiza o formulário de edição
    #retorna uma lista que contém os detalhes da música selecionada para edição.
@app.route('/apagar_musica/<int:codigo>')
def apagar_musica(codigo):

    del musica[codigo]
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)