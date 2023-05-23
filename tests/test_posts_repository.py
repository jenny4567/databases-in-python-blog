from lib.posts_repository import PostRepository
from lib.posts import Post
from lib.comments import Comment

"""
When we call PostRepository#all
We get a list of post objects reflecting the seed data.
"""
def test_get_all_posts(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/blogger.sql") # Seed our database with some test data
    repository = PostRepository(db_connection) # Create a new PostRepository

    posts = repository.all() # Get all Posts

    # Assert on the results
    assert posts == [
        Post(1, 'Day 1', 'First day at work.'),
        Post(2, 'Happy Birthday', 'My brothers birthday.'),
        Post(3, 'First pet', 'Got my first dog!'),
        Post(4, 'Day 5', 'Last day at work.')
    ]

"""
When we call PostRepository#find
We get a single post object reflecting the seed data.
"""
def test_get_single_post(db_connection):
    db_connection.seed("seeds/blogger.sql")
    repository = PostRepository(db_connection)

    post = repository.find(3)
    assert post == Post(3, 'First pet', 'Got my first dog!')

"""
When we call PostRepository#create
We get a new post in the database.
"""
def test_create_post(db_connection):
    db_connection.seed("seeds/blogger.sql")
    repository = PostRepository(db_connection)

    repository.create(Post(None, 'My divorce', 'I am getting divorced.'))

    result = repository.all()
    assert result == [
        Post(1, 'Day 1', 'First day at work.'),
        Post(2, 'Happy Birthday', 'My brothers birthday.'),
        Post(3, 'First pet', 'Got my first dog!'),
        Post(4, 'Day 5', 'Last day at work.'),
        Post(5, 'My divorce', 'I am getting divorced.')
    ]

"""
When we call PostRepository#delete
We remove a post from the database.
"""
def test_delete_post(db_connection):
    db_connection.seed("seeds/blogger.sql")
    repository = PostRepository(db_connection)
    repository.delete(1) 
    
    result = repository.all()
    assert result == [
        Post(2, 'Happy Birthday', 'My brothers birthday.'),
        Post(3, 'First pet', 'Got my first dog!'),
        Post(4, 'Day 5', 'Last day at work.')
    ]

"""
When I call #find_with_comments with a post_id
Then I get the post with a list of comments, prepopulated.
"""
def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blogger.sql")
    repository = PostRepository(db_connection)

    post = repository.find_with_comments(3)
    assert post == Post(3, 'First pet', 'Got my first dog!', [
        Comment(3, 'DogLover', 'What breed?', 3),
        Comment(5, 'AnimalLover5', 'Just got a new pet too.', 3)
    ])


