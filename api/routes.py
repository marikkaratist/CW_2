from flask import Blueprint, jsonify
from config import Config
from app.posts.dao.posts_dao import PostsDAO
import logging


directory = Config()
posts_manager = PostsDAO(directory.POSTS)
api_blueprint = Blueprint("api_blueprint", __name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(directory.LOGGER, encoding="utf-8")
formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


@api_blueprint.route("/posts")
def get_posts():
    logger.info("Запрос /api/posts")
    posts = posts_manager.get_all()

    return jsonify(posts)


@api_blueprint.route("/posts/<int:post_id>")
def get_post_by_pk(post_id):
    post = posts_manager.get_by_pk(post_id)
    logger.info("Запрос/api/posts/%s", post_id)

    return jsonify(post)
