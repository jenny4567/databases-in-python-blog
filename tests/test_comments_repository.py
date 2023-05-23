from lib.comments_repository import CommentRepository
from lib.comments import Comment

"""
When we call CommentRepository#all
We get a list of comment objects reflecting the seed data.
"""
def test_get_all_comments(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/blogger.sql") # Seed our database with some test data
    repository = CommentRepository(db_connection) # Create a new CommentRepository

    comments = repository.all() # Get all Comments

    # Assert on the results
    assert comments == [
        Comment(1, 'username123', 'Wow, it was my first day too!', 1),
        Comment(2, 'Jammydodger789', 'Happy birthday!', 2),
        Comment(3, 'DogLover', 'What breed?', 3),
        Comment(4, 'JohnM1994', 'Good luck at your new job!', 4),
        Comment(5, 'AnimalLover5', 'Just got a new pet too.', 3)
    ]

"""
When we call CommentRepository#find
We get a single comment object reflecting the seed data.
"""
def test_get_single_comment(db_connection):
    db_connection.seed("seeds/blogger.sql")
    repository = CommentRepository(db_connection)

    comment = repository.find(3)
    assert comment == Comment(3, 'DogLover', 'What breed?', 3)

"""
When we call CommentRepository#create
We get a new comment in the database.
"""
def test_create_comment(db_connection):
    db_connection.seed("seeds/blogger.sql")
    repository = CommentRepository(db_connection)

    repository.create(Comment(None, 'SnakeLover88', 'I am also getting a new snake!', 3))

    result = repository.all()
    assert result == [
        Comment(1, 'username123', 'Wow, it was my first day too!', 1),
        Comment(2, 'Jammydodger789', 'Happy birthday!', 2),
        Comment(3, 'DogLover', 'What breed?', 3),
        Comment(4, 'JohnM1994', 'Good luck at your new job!', 4),
        Comment(5, 'AnimalLover5', 'Just got a new pet too.', 3),
        Comment(6, 'SnakeLover88', 'I am also getting a new snake!', 3)
    ]

"""
When we call CommentRepository#delete
We remove a comment from the database.
"""
def test_delete_comment(db_connection):
    db_connection.seed("seeds/blogger.sql")
    repository = CommentRepository(db_connection)
    repository.delete(1) 
    
    result = repository.all()
    assert result == [
        Comment(2, 'Jammydodger789', 'Happy birthday!', 2),
        Comment(3, 'DogLover', 'What breed?', 3),
        Comment(4, 'JohnM1994', 'Good luck at your new job!', 4),
        Comment(5, 'AnimalLover5', 'Just got a new pet too.', 3)
    ]