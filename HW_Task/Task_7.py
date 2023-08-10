
'''
Задание №7
Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через контекст.
'''

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/news/')
def news():
    news = [{"heading": "Когда мире наступит мир!",
             'description': 'Данная статья о мире во всем Мире',
             "date": "09.08.2023"},
            {"heading": "Утята!",
             'description': 'Данная статья о том как утята учатся летать',
             "date": "08.05.2022"},
            {"heading": "Корабли!",
             'description': 'Данная статья о черноморском флоте',
             "date": "16.02.2022"},]

    return render_template("news.html", news=news)

if __name__ == '__main__':
    app.run(debug=True)