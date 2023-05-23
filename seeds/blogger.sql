
DROP TABLE IF EXISTS comments cascade;
DROP SEQUENCE IF EXISTS comments_id_seq;
DROP TABLE IF EXISTS posts cascade;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text
);

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS comments_id_seq;
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    username text,
    content text, 
-- The foreign key name is always {other_table_singular}_id
    post_id int,
    constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);


INSERT INTO posts (title, content) VALUES ('Day 1', 'First day at work.');
INSERT INTO posts (title, content) VALUES ('Happy Birthday', 'My brothers birthday.');
INSERT INTO posts (title, content) VALUES ('First pet', 'Got my first dog!');
INSERT INTO posts (title, content) VALUES ('Day 5', 'Last day at work.');

INSERT INTO comments (username, content, post_id) VALUES ('username123', 'Wow, it was my first day too!', 1);
INSERT INTO comments (username, content, post_id) VALUES ('Jammydodger789', 'Happy birthday!', 2);
INSERT INTO comments (username, content, post_id) VALUES ('DogLover', 'What breed?', 3);
INSERT INTO comments (username, content, post_id) VALUES ('JohnM1994', 'Good luck at your new job!', 4);
INSERT INTO comments (username, content, post_id) VALUES ('AnimalLover5', 'Just got a new pet too.', 3);