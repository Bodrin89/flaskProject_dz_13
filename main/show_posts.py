#Импорт функций
from utils import read_json_file, load_posts

#импортируем класс блюпринта
from flask import render_template, Blueprint, request

FILE = 'posts.json'
#data_list = read_json_file(FILE)

#создаем новый блюпринт, выбираем для него имя
show_foto_blueprint = Blueprint('show_foto_blueprint', __name__)
search_post_blueprint = Blueprint('search_post_blueprint', __name__)


@show_foto_blueprint.route('/')
def home_page():
    index = render_template('index.html')
    return f'{index}'


@search_post_blueprint.route('/search')
def search_post():
    s = request.args.get('s')
    data_list = read_json_file(FILE)
    post = render_template('post_list.html', all_search_posts=load_posts(s, data_list))
    return f'{post}'


