class Comment():
    def __init__(self, id, username, content, post_id):
        self.id = id
        self.username = username
        self.content = content
        self.post_id = post_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Comment({self.id}, {self.username}, {self.content}, {self.post_id})"