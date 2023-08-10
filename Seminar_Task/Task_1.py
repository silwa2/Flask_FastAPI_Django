from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello Word'


@app.route('/about/')
def about():
    return 'about'


@app.route('/contact/')
def contact():
    return 'contact'


@app.route('/sum/<int:a>+<int:b>/')
def sum1(a, b):
    rez = a + b
    return f'{a}+{b} = {rez}'


@app.route('/text/<text>/')
def text(text):
    return f'Длина строки {text} = {len(text)}'


@app.route("/first-page/")
def first_page():
    return ("<h1>Моя первая HTML страница</h1>"
            "<p>Привет, мир!</p>")


if __name__ == '__main__':
    app.run(debug=True)
