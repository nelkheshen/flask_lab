# GitHub Repo: https://github.com/nelkheshen/flask_lab
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return '''
    Hello world
    <p>Adam Y. : idk-quick and easy response</p>
    <p>Amir K. : wtf-likes that it is expressive</p>
    <p>Maddi L. : lmao-uses it alot</p>
    '''
@app.route('/nadine')
def nadine():
    return render_template(
        'template.html',
        name= "Nadine",
        acronym= 'lol'
    )
