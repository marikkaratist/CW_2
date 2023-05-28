import json


class PostsDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data

    def get_all(self):
        """Возвращает все посты"""
        posts = self.load_data()

        return posts

    def get_by_user(self, user_name):
        """Возвращает посты определенного пользователя"""
        posts = self.load_data()
        posts_list = []

        for post in posts:
            if user_name in post["poster_name"]:
                posts_list.append(post)

        if not posts_list:
            raise ValueError("Такого пользователя нет")

        return posts_list

    def get_by_post_id(self, post_id):
        """Возвращает комментарии определенного поста"""
        comments = self.load_data()
        comments_list = []

        for comment in comments:
            if comment["post_id"] == post_id:
                comments_list.append(comment)

        if not comments_list:
            raise ValueError("Такого поста нет")

        return comments_list

    def get_by_text(self, query):
        """Возвращает список постов по ключевому слову"""
        posts = self.load_data()
        posts_list = []

        for post in posts:
            query_lower = query.lower()
            if query_lower in post["content"].lower():
                posts_list.append(post)

        return posts_list

    def get_by_pk(self, pk):
        """Возвращает один пост по его идентификатору"""
        posts = self.load_data()
        found_post = None

        for post in posts:
            if pk == post["pk"]:
                found_post = post
                break

        return found_post
