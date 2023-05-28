from flask import Flask
from app.posts.views import posts_blueprint
from api.routes import api_blueprint

app = Flask(__name__)
app.register_blueprint(posts_blueprint)
app.register_blueprint(api_blueprint, url_prefix="/api")


@app.errorhandler(404)
def page_not_found(error):

    return "Страница не найдена", 404


@app.errorhandler(500)
def internal_server_error(error):

    return "Внутренняя ошибка сервера", 500


@app.route('/error')
def raise_error():
    # Пример ошибки на стороне сервера

    raise Exception("Произошла ошибка на стороне сервера")


if __name__ == "__main__":
    app.run()
