import logging
import uuid
from flask import Blueprint, render_template, request
from utils import check_extension, load_new_post, read_json_file

load_post_blueprint = Blueprint('load_post_blueprint', __name__)
save_foto_blueprint = Blueprint("save_foto_blueprint", __name__)
save_text_blueprint = Blueprint("save_text_blueprint", __name__)

FILE = 'posts.json'
data_list = read_json_file(FILE)
ALL_EXTENSION = ['png', 'jpeg', 'jpg']


@load_post_blueprint.route('/post')
def load_page():
    load_file = render_template('post_form.html')
    return load_file


@save_foto_blueprint.route("/post", methods=['POST'])
def save_foto():
    foto = request.files.get('picture')
    text = request.form.get('new_post')
    file_extension = foto.content_type.split('/')[-1]
    if foto:
        if check_extension(ALL_EXTENSION, file_extension):
            path_img = f'static/img/{uuid.uuid4()}.{file_extension}'
            foto.save(path_img)
            new_json_data = {
                "pic": path_img,
                "content": f"{text}"
            }
            load_new_post(new_json_data, data_list, FILE)
            ff = [new_json_data]
            index_page = render_template('post_list.html', all_search_posts=ff)
            return f"{index_page}"
        else:
            logging.info('файл не фото')
            return 'файл не фото'
    else:
        return 'Файла нет'



