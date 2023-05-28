from flask import Blueprint, request, render_template
from .dao.posts_dao import PostsDAO
from config import Config

directory = Config()
posts_blueprint = Blueprint("posts_blueprint", __name__, template_folder="templates")
posts_manager = PostsDAO(directory.POSTS)
comments_manager = PostsDAO(directory.COMMENTS)


@posts_blueprint.route("/")
def page_main():
    posts = posts_manager.get_all()

    return render_template("index.html", posts=posts)


@posts_blueprint.route("/user/<user_name>")
def page_user_feed(user_name):
    posts = posts_manager.get_by_user(user_name)

    return render_template("user-feed.html", posts=posts, user_name=user_name)


@posts_blueprint.route("/posts/<int:post_id>")
def page_post(post_id):
    post = posts_manager.get_by_pk(post_id)
    comments = comments_manager.get_by_post_id(post_id)
    comments_number = len(comments)

    return render_template("post.html", post=post, comments=comments, comments_number=comments_number)


@posts_blueprint.route("/search")
def page_post_search():
    s = request.args.get("s", "")
    posts = posts_manager.get_by_text(s)
    posts_number = len(posts)

    return render_template("search.html", posts=posts, s=s, posts_number=posts_number)

