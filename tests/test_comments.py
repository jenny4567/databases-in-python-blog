from lib.comments import Comment 

"""
Comment constructs with an id, username and content and post_id
"""
def test_comment_constructs():
    comment = Comment(1, "Test Username", "Test Content", "Test Post_id")
    assert comment.id == 1
    assert comment.username == "Test Username"
    assert comment.content == "Test Content"
    assert comment.post_id == "Test Post_id"

"""
We can format comments to strings nicely
"""
def test_comments_format_nicely():
    comment = Comment(1, "Test Username", "Test Content", "Test Post_id")
    assert str(comment) == "Comment(1, Test Username, Test Content, Test Post_id)"


"""
We can compare two identical comments
And have them be equal
"""
def test_comments_are_equal():
    comment1 = Comment(1, "Test Username", "Test Content", "Test Post_id")
    comment2 = Comment(1, "Test Username", "Test Content", "Test Post_id")
    assert comment1 == comment2