
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

    # Insert the data into the users table
    for user in users_data:
        cur.execute(
            "INSERT INTO users (id, age, country, gender) VALUES (%s, %s, %s, %s)",
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
