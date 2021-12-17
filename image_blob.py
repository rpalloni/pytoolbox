import base64 # https://www.base64encoder.io/learn/
from PIL import Image
from io import BytesIO
from psycopg2 import connect # POSTGRES

# set up db connection and create sample table with BLOB field
try:
    with connect(
        host='localhost',
        port='5555',
        database='db',
        user=input('Enter username: '),
        password=input('Enter password: '),
    ) as connection:
        print(connection)
except Exception as e:
    print(e)

# WARNING: BYTEA is Postgres BLOB
create_table_query = '''CREATE TABLE PROFILE ( ID BIGINT PRIMARY KEY, NAME VARCHAR(50) NOT NULL, PICTURE BYTEA NOT NULL );'''
with connection.cursor() as cursor:
    cursor.execute(create_table_query)

###################### INSERT RECORD WITH BLOB FILED ##########################

cursor = connection.cursor()
file = open('photo.jpg', 'rb').read() # open a file in binary mode
file_data = base64.b64encode(file) # encode the file to get base64 string
type(file_data)
print(file_data) # b'xxxxxxx'
print(file_data.decode('utf-8')) # str

record = ('100', 'Jack Foo', file_data)
query = 'INSERT INTO PROFILE VALUES(%s, %s, %s)'

cursor.execute(query, record)
connection.commit()

###################### RETRIEVE RECORD WITH BLOB FILED ##########################

cursor = connection.cursor()
query = 'SELECT PICTURE FROM PROFILE WHERE ID=100'

cursor.execute(query)
data = cursor.fetchall()

image = data[0][0] # returned data will be a list of list

binary_data = base64.b64decode(image) # decode the string
type(binary_data)
print(binary_data)
print(base64.b64encode(binary_data).decode('utf-8')) # str

image = Image.open(BytesIO(binary_data)) # Convert the bytes into a PIL image
image.show()
