

import psycopg2
import json

def create_users_table(connection_info):
    conn = psycopg2.connect(**connection_info)
    cur = conn.cursor()

    # Creating table
    query = '''
    CREATE TABLE IF NOT EXISTS users(
        id INT PRIMARY KEY,
        age INT,
        country VARCHAR(255),
        gender VARCHAR(50)
    )
    '''
    cur.execute(query)
    
    # Open and load the data from the JSON file
    with open('users.json') as f:
        users_data = json.load(f)

    for user in users_data:
        cur.execute(
            """
            INSERT INTO users (id, age, country, gender) VALUES (%s, %s, %s, %s)
            ON CONFLICT (id) 
            DO NOTHING
            """,
            (user['id'], user['age'], user['country'], user['gender'])
        )

    # Committing the transaction and closing the connection
    conn.commit()
    cur.close()
    conn.close()

# Database connection parameters
connection_info = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Perceptron",
    "host": "localhost",
    "port": 5433  # or any port you have configured
}

# Creating table and inserting data
create_users_table(connection_info)



import psycopg2
import json
from datetime import datetime

def create_items_table(connection_info):
    conn = psycopg2.connect(**connection_info)
    cur = conn.cursor()

    # Creating table
    query = '''
    CREATE TABLE IF NOT EXISTS items(
        bucket_key VARCHAR(255),
        created_at TIMESTAMP,
        item_key UUID PRIMARY KEY,
        type VARCHAR(255),
        user_id INT
    )
    '''
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()


def insert_items_data(connection_info):
    conn = psycopg2.connect(**connection_info)
    cur = conn.cursor()

    # Open and load the data from the JSON file
    with open('items0.json') as f:
        items_data = json.load(f)

    # Insert the data into the items table
    
    for item in items_data:
        created_at = datetime.strptime(item['created_at'], "%a, %d %b %Y %H:%M:%S %Z")
        cur.execute(
            """
            INSERT INTO items (bucket_key, created_at, item_key, type, user_id) VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (item_key) 
            DO NOTHING
            """,
            (item['bucket_key'], created_at, item['item_key'], item['type'], item['user_id'])
        )

    # Committing the transaction and closing the connection
    conn.commit()
    cur.close()
    conn.close()


# Database connection parameters
connection_info = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Perceptron",
    "host": "localhost",
    "port": 5433  # or any port you have configured
}

# Creating table
create_items_table(connection_info)

# Inserting data
insert_items_data(connection_info)

