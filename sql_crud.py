# postgres
import psycopg2
from psycopg2 import sql, connect

try:
    with connect(
        host='localhost',
        port='5432',
        database='books',
        user=input('Enter username: '), # user
        password=input('Enter password: '), # pwd
    ) as connection:
        print(connection)
except Exception as e:
    print(e)

''' db schema
    BOOKS       RATINGS         REVIEWERS
    id          id              id
    title       book_id         first_name
    genre       reviewer_id     last_name
    release     rating          age

books and reviewers will have a many-to-many relationship since
one book can be reviewed by multiple reviewers and one reviewer
can review multiple books.
The ratings table connects the books table with the reviewers table.
'''

################################ create schema ############################

create_books_table_query = '''
CREATE TABLE books(
    id serial PRIMARY KEY,
    title VARCHAR(100),
    genre VARCHAR(100),
    release INTEGER
);
'''

# pk shorter syntax
create_reviewers_table_query = '''
CREATE TABLE reviewers(
    id serial PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    age INTEGER
);
'''

create_ratings_table_query = '''
CREATE TABLE ratings(
    book_id INT,
    reviewer_id INT,
    rating INTEGER,
    PRIMARY KEY(book_id, reviewer_id),
    FOREIGN KEY(book_id) REFERENCES books(id),
    FOREIGN KEY(reviewer_id) REFERENCES reviewers(id)
)
'''
with connection.cursor() as cursor:
    cursor.execute(create_books_table_query)
    cursor.execute(create_reviewers_table_query)
    cursor.execute(create_ratings_table_query)
    connection.commit()

show_table_query = '''
SELECT
   table_name,
   column_name,
   data_type
FROM
   information_schema.columns
WHERE
   table_name = 'books';
'''

with connection.cursor() as cursor:
    cursor.execute(show_table_query)
    # Fetch rows from last executed query
    result = cursor.fetchall()
    for row in result:
        print(row)

################################ insert data ###############################

insert_books_query = '''
INSERT INTO books (title, release, genre)
VALUES
    ('Forrest Gump', 1994, 'Drama'),
    ('Skyfall', 2012, 'Action'),
    ('Gladiator', 2000, 'Action'),
    ('Casablanca', 1942, 'Romance'),
    ('3 Idiots', 2009, 'Drama'),
    ('Black', 2005, 'Drama'),
    ('Titanic', 1997, 'Romance'),
    ('The Shawshank Redemption', 1994, 'Drama'),
    ('Man in black', 1997, 'Action'),
    ('Udaan', 2010, 'Drama'),
    ('Home Alone', 1990, 'Comedy'),
    ('Good Will Hunting', 1997, 'Drama')
'''
with connection.cursor() as cursor:
    cursor.execute(insert_books_query)
    connection.commit()


insert_reviewers_query = '''
INSERT INTO reviewers
(first_name, last_name, age)
VALUES ( %s, %s, %s )
'''
reviewers_records = [
    ('Chaitanya', 'Baweja', 26),
    ('Mary', 'Cooper', 45),
    ('John', 'Wayne', 34),
    ('Thomas', 'Stoneman', 29),
    ('Penny', 'Hofstadter', 38),
    ('Mitchell', 'Marsh', 51),
    ('Wyatt', 'Skaggs', 52),
    ('Andre', 'Veiga', 49),
    ('Sheldon', 'Cooper', 45),
    ('Kimbra', 'Masters', 43),
    ('Kat', 'Dennings', 61),
    ('Bruce', 'Wayne', 18),
    ('Domingo', 'Cortes', 42),
    ('Rajesh', 'Koothrappali', 33),
    ('Ben', 'Glocker', 19),
    ('Mahinder', 'Dhoni', 20),
    ('Akbar', 'Khan', 22),
    ('Howard', 'Wolowitz', 27),
    ('Pinkie', 'Petit', 28),
    ('Gurkaran', 'Singh', 38),
    ('Amy', 'Farah Fowler', 41),
    ('Marlon', 'Crafford', 45),
]
with connection.cursor() as cursor:
    cursor.executemany(insert_reviewers_query, reviewers_records)
    connection.commit()


insert_ratings_query = '''
INSERT INTO ratings
(rating, book_id, reviewer_id)
VALUES ( %s, %s, %s)
'''
ratings_records = [
    (6, 7, 5), (5, 9, 1), (6, 2, 14), (5, 2, 17),
    (5, 5, 5), (6, 3, 5), (8, 3, 13), (9, 6, 4),
    (8, 4, 12), (9, 4, 9), (8, 6, 14), (9, 12, 10),
]
with connection.cursor() as cursor:
    cursor.executemany(insert_ratings_query, ratings_records)
    connection.commit()

################################ select data ###############################

select_all_books_query = "SELECT * FROM books ORDER BY release DESC"
with connection.cursor() as cursor:
    cursor.execute(select_all_books_query)
    result = cursor.fetchall()
    for row in result:
        print(row)


with connection.cursor() as cursor:
    cursor.execute(select_all_books_query)
    result = cursor.fetchmany(size=2)
    for row in result:
        print(row)


select_books_query = '''
SELECT title, AVG(rating) as average_rating
FROM ratings, books
WHERE books.id = ratings.book_id
GROUP BY book_id, title
ORDER BY average_rating DESC
'''

with connection.cursor() as cursor:
    cursor.execute(select_books_query)
    for row in cursor.fetchall():
        print(row)

################################ update data ###############################
update_query = '''
UPDATE
    reviewers
SET
    last_name = 'Cooper'
WHERE
    first_name = 'Amy'
'''

with connection.cursor() as cursor:
    cursor.execute(update_query)
    connection.commit()

# compose query
book = input('Enter book id: ')
rev = input('Enter reviewer id: ')
new_rating = input('Enter new rating: ')
update_query = '''
UPDATE
    ratings
SET
    rating = %s
WHERE
    book_id = %s AND reviewer_id = %s;
'''
val_tuple = (new_rating, book, rev)

with connection.cursor() as cursor:
    cursor.execute(update_query, val_tuple)
    connection.commit()


delete_query = "DELETE FROM ratings WHERE reviewer_id = 2"
with connection.cursor() as cursor:
    cursor.execute(delete_query)
    connection.commit()

connection.close()
