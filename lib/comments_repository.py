from lib.comments import Comment

class CommentRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from comments')
        comments = []
        for row in rows:
            item = Comment(row["id"], row["username"], row["content"], row["post_id"])
            comments.append(item)
        return comments
    
    def find(self, comment_id):
        rows = self._connection.execute(
            'SELECT * from comments WHERE id = %s', [comment_id])
        row = rows[0]
        return Comment(row["id"], row["username"], row["content"], row["post_id"])
    
    def create(self, comment):
        self._connection.execute('INSERT INTO comments (username, content, post_id) VALUES (%s, %s, %s)', [
                                comment.username, comment.content, comment.post_id])
        return None
    
    def delete(self, comment_id):
        self._connection.execute(
            'DELETE FROM comments WHERE id = %s', [comment_id])
        return None