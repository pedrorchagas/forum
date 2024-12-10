from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from markupsafe import escape
import accountManager

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',  methods=('GET','POST'))
def login():

    if request.method == 'POST':
        print(request.form.to_dict())
        data = request.form.to_dict()
        accountManager.login(email=data['email'], password=data['password'])

        return render_template('login.html')

    return render_template('login.html')

@app.route('/cadastrar', methods=('GET', 'POST'))
def cadastrar():
    
    if request.method == 'POST':
        data = request.form.to_dict()

        name = data['user']
        email = data['email']
        password1 = data['password']
        password2 = data['password-c']

        if password1 != password2:
            print('senha não bate')
            return render_template('cadastrar.html')
            

        registred = accountManager.signUp(name, email, password1)
        if registred:
            return render_template('cadastrar.html', cadastrado=request.form.to_dict())
        else:
            print('erro no cadastro')
            return render_template('cadastrar.html')

    


    return render_template('cadastrar.html')

@app.route('/curso/<arquivo>')
def curso(arquivo):
    # caminho para testar meinhas habilidades
    return render_template(f"/curso/{escape(arquivo)}", )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")