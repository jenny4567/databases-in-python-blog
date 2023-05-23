from lib.posts import Post

"""
Post constructs with an id, title and content
"""
def test_post_constructs():
    post = Post(1, "Test Title", "Test Content", "Test Comments")
    assert post.id == 1
    assert post.title == "Test Title"
    assert post.content == "Test Content"
    assert post.comments == "Test Comments"

"""
We can format post to strings nicely
"""
def test_posts_format_nicely():
    post = Post(1, "Test Title", "Test Content", "Test Comments")
    assert str(post) == "Post(1, Test Title, Test Content, Test Comments)"

"""
We can compare two identical posts
And have them be equal
"""
def test_posts_are_equal():
    post1 = Post(1, "Test Title", "Test Content", "Test Comments")
    post2 = Post(1, "Test Title", "Test Content", "Test Comments")
    assert post1 == post2