from flask  import *
from flask import jsonify


import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify



app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(host='localhost:3306', database='todo', user='root', password='root')
        if conn.is_connected():
            print('Connected to MySQL database')

            # Get user details from request
            data = request.get_json()
            email = data['email']
            password = data['password']
            username = data['usernmae']

            # Insert user details into database
            cursor = conn.cursor()
            query = "INSERT INTO users (email, password,username) VALUES (%s, %s, %s)"
            values = ( email, password, username)
            cursor.execute(query, values)
            conn.commit()
            print('User registered successfully')
            cursor.close()

            # Return success message
            return jsonify({'message': 'User registered successfully'})

    except Error as e:
        print(e)

    finally:
        # Close database connection
        conn.close()

if __name__=='__main__':
     app.run(port='7775')