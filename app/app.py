from fastapi import FastAPI, Request, HTTPException
import psycopg2
import json

app = FastAPI()

connection_info = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "Perceptron",
    "host": "localhost",
    "port": 5433  # or any port you have configured
}


@app.get('/')
async def read_root(request: Request):
    headers = request.headers
    userid = headers.get('user')

    if userid is None:
        raise HTTPException(status_code=400, detail="User header is missing")
    
    item = item_returner(connection_info, userid)
    return item


def item_returner(connection_info, userid):
    conn = psycopg2.connect(**connection_info)
    cur = conn.cursor()

    cur.execute(
        """
        SELECT item_key FROM items WHERE user_id = %s
        """,
        (userid,)  # Notice the comma, making it a tuple
    )
    item_keys = cur.fetchall()

    cur.close()
    conn.close()

    return item_keys


















    return '0007933c-e702-4ccf-872c-d5235d6ee51a'






















@app.post('/evt')
def read_event(request: Request):
    headers = request.headers
    for key, value in headers.items():
        print(f"{key}:{value}")
        
    
    return 'Hello from event route'