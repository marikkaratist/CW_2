from run import app
keys_post_should_be = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk",
}


def test_get_posts():
    response = app.test_client().get("/api/posts")

    assert response.status_code == 200
    assert isinstance(response.json, list)
    assert set(response.json[0]) == keys_post_should_be


def test_get_post_by_pk():
    response = app.test_client().get("/api/posts/4")

    assert response.status_code == 200
    assert isinstance(response.json, dict)
    assert set(response.json) == keys_post_should_be
