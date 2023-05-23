class Post():
    def __init__(self, id, title, content, comments = None):
        self.id = id
        self.title = title
        self.content = content
        self.comments = comments or []
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.comments})"