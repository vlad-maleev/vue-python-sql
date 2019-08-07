from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os
import sys 
import argparse


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

def createTable(): 
    con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="qwertyasD",
        host="localhost"
    )

    cur = con.cursor()

    name_Table = "file_storage"

    sqlCreateTable = "create table "+name_Table+" (orig_filename text not null, file_data bytea not null);"

    cur.execute(sqlCreateTable)
    con.commit()

def getData():
    con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="qwertyasD",
        host="localhost"
    )

    cur = con.cursor()

    cur.execute('select * from file_storage')

    file_records = cur.fetchall() 
   
    for row in file_records:
       print("id = ", row[0], )
       print("name = ", row[1])
       print("file = ", row[2], "\n")

    cur.close()
    con.close()

# getData() #getting data from file_storage table
       


# create_table_stm = """
# CREATE TABLE files (
#     orig_filename text not null,
#     file_data bytea not null
# )
# """

# reading image
# fin = open("C:\\Users\\VladMaleev\\Desktop\\vue-python-sql\\server\\aj.png", "rb") 

# def readImage():
#     try:
#         img = fin.read()
#         return img

#     except IOError as e:
#         # print "Error %d: %s" % (e.args[0],e.args[1])
#         sys.exit(1)

#     finally:
#         if fin:
#             fin.close()
# try:
#     con = psycopg2.connect( 
#         database="postgres",
#         user="postgres",
#         password="qwertyasD",
#         host="localhost")
#     cur = con.cursor()
#     data = readImage()
#     binary = psycopg2.Binary(data)
#     cur.execute("INSERT INTO file_storage(id, orig_filename, file_data) VALUES (1, %s, %s)", ("file", binary) )
#     con.commit()
# except psycopg2.DatabaseError as e:
#     if con:
#         con.rollback()
#     # print "Error %s" % e    
#     sys.exit(1)
# finally: 
#     if con:
#         con.close()



# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# BOOKS = [
#     {
#         'title': 'On the Road',
#         'author': 'Jack Kerouac',
#         'read': True
#     },
#     {
#         'title': 'Harry Potter and the Philosopher\'s Stone',
#         'author': 'J. K. Rowling',
#         'read': False
#     },
#     {
#         'title': 'Green Eggs and Ham',
#         'author': 'Dr. Seuss',
#         'read': True
#     }
# ]

# @app.route('/books', methods=['GET', 'POST'])
# def all_books():
#     response_object = {'status': 'success'}

#     if request.method == 'POST':
#         post_data = request.get_json()
#         BOOKS.append({
#             'title': post_data.get('title'),
#             'author': post_data.get('author'),
#             'read': post_data.get('read')
#         })
#         response_object['message'] = 'Book added!'
#     else:
#         response_object['books'] = BOOKS
#     return jsonify(response_object)



@app.route('/upload', methods=['GET', 'POST'])
def upload():
    response_object = {'status': 'success'}
    
    if request.method == 'POST':
        try:
            con = psycopg2.connect( 
                database="postgres",
                user="postgres",
                password="qwertyasD",
                host="localhost"
            )
            cur = con.cursor()
            file = request.data
            #binary = psycopg2.Binary(data)
            cur.execute("INSERT INTO file_storage(orig_filename, file_data) VALUES (%s, %s)", ("example file", file) )
            con.commit()

        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            #print "Error %s" % e    
            sys.exit(1)
        finally: 
            if con:
                con.close()

        return jsonify(response_object)
    # if request.method == 'POST':
    #     return jsonify(request.data)
    



if __name__ == '__main__':
    app.run()

