from flask import Flask, render_template, request
from main.show_posts import show_foto_blueprint, search_post_blueprint
from loader.load_file import load_post_blueprint, save_foto_blueprint

app = Flask(__name__)


app.register_blueprint(show_foto_blueprint)
app.register_blueprint(search_post_blueprint)
app.register_blueprint(load_post_blueprint)
app.register_blueprint(save_foto_blueprint)


if __name__ == '__main__':
    app.run()
