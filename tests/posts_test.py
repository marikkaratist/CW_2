import pytest
from app.posts.dao.posts_dao import PostsDAO
from config import Config

directory = Config()
keys_post_should_be = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk",
}
keys_comments_should_be = {
    "post_id",
    "commenter_name",
    "comment",
    "pk",
}


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO(directory.POSTS)
    return posts_dao_instance


@pytest.fixture()
def comments():
    comments_instance = PostsDAO(directory.COMMENTS)
    return comments_instance


class TestPostsDAO:

    def test_get_all(self, posts_dao):
        posts = posts_dao.get_all()
        assert type(posts) == list, "Возвращается не список"
        assert len(posts) > 0, "Возвращается пустой список"
        assert set(posts[0].keys()) == keys_post_should_be, "Ключи не соответствуют требуемым"

    def test_get_by_user(self, posts_dao):
        with pytest.raises(ValueError):
            posts_dao.get_by_user("donald")
        posts = posts_dao.get_by_user(user_name="hank")
        assert type(posts) == list, "Возвращается не список"
        assert set(posts[0].keys()) == keys_post_should_be, "Ключи не соответствуют требуемым"

    def test_get_by_post_id(self, comments):
        with pytest.raises(ValueError):
            comments.get_by_post_id(9)
        comments_list = comments.get_by_post_id(post_id=7)
        assert type(comments_list) == list, "Возвращается не список"
        assert set(comments_list[0].keys()) == keys_comments_should_be, "Ключи не соответствуют требуемым"

    def test_get_by_text(self, posts_dao):
        posts = posts_dao.get_by_text(query="утро")
        assert type(posts) == list, "Возвращается не список"
        assert len(posts) > 0, "Возвращается пустой список"
        assert set(posts[0].keys()) == keys_post_should_be, "Ключи не соответствуют требуемым"

    def test_get_by_pk(self, posts_dao):
        posts = posts_dao.get_by_pk(pk=2)
        assert type(posts) == dict, "Возвращается не список"
        assert len(posts) > 0, "Возвращается пустой список"
        assert posts["pk"] == 2, "Возвращается неверный идентификатор поста"
        assert set(posts.keys()) == keys_post_should_be, "Ключи не соответствуют требуемым"
