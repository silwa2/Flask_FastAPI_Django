from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Привет, незнакомец!'


@app.route('/Николай/')
def nike():
    return 'Привет, Николай!'


@app.route('/Иван/')
def ivan():
    return 'Привет, Ванечка!'

@app.route('/poems/')
def poems():
    poem = ['Вот не думал, не гадал,',
    'Программистом взял и стал.',
    'Хитрый знает он язык,',
    'Он к другому не привык.',
    ]
    txt = '<h1>Стихотворение</h1>\n<p>' + '<br/>'.join(poem) +'</p>'
    return txt

if __name__ == '__main__':
    app.run()

