class Post():
    POSTS = [
        {"id": 1, "title": "First Post", "body": "this is my first post"},
        {"id": 2, "title": "Second Post", "body": "this is my Second post"},
        {"id": 3, "title": "Third Post", "body": "this is my Third post"},
    ]


    def all(self):
        return self.POSTS

    def find(cls, id):
        return cls.POSTS[int(id)-1]