from lib.posts import Post
from lib.comments import Comment

class PostRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * from posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["content"])
            posts.append(item)
        return posts

    def find(self, post_id):
        rows = self._connection.execute(
            'SELECT * from posts WHERE id = %s', [post_id])
        row = rows[0]
        return Post(row["id"], row["title"], row["content"])
    
    def find_with_comments(self, post_id):
        rows = self._connection.execute(
            'SELECT posts.id as post_id, posts.title, posts.content as post_content, comments.id, comments.username, comments.content as comment_content, comments.post_id FROM posts JOIN comments ON posts.id = comments.post_id WHERE posts.id = %s', [post_id]
        )
        comments = []
        for row in rows:
            comment = Comment(row['id'], row['username'], row['comment_content'], row['post_id'])
            #print(comment)
            comments.append(comment)
            #print(comments)
            post = Post(rows[0]['post_id'], rows[0]['title'], rows[0]['post_content'], comments)
        print(post)
        return post


    def create(self, post):
        self._connection.execute('INSERT INTO posts (title, content) VALUES (%s, %s)', [
                                post.title, post.content])
        return None
    
    def delete(self, post_id):
        self._connection.execute(
            'DELETE FROM posts WHERE id = %s', [post_id])
        return None
    
