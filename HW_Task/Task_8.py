'''
Задание №8
Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна (шапка, меню, подвал),
и дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.
'''

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/cap/')
def cap():

    return render_template("Cap.html")

@app.route("/about/")
def about():


    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)
