from fastapi import FastAPI, Request, HTTPException
import redis
import pg8000
import json

app = FastAPI()

@app.get('/')
async def read_root(request: Request):
    headers = request.headers
    userid = headers.get('user')
    session = headers.get('session')

    connection_info = {
    "database": "postgres",
    "user": "postgres",
    "password": "Perceptron",
    "host": "localhost",
    "port": 5433  # or any port you have configured
    }
    
    if userid is None or session is None:
        raise HTTPException(status_code=400, detail="Missing user or session in headers")

    r = redis.Redis(host='cache', port=6380, decode_responses=True)
    r.set(f"user:{session}", userid)
    r.set(f"session:{session}", session)
    r.hset(f'user-session:{session}', mapping={
        'name': 'John',
        "surname": 'Smith',
        "company": 'Redis',
        "age": 29
    })
    
    def item_returner(connection_info, userid):
        conn = pg8000.connect(**connection_info)
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

    item = item_returner(connection_info, userid)

    user_data = r.hgetall(f'user-session:{session}')

    # return {"item": item, "user_data": user_data}
    return {"item": item,}

@app.post('/evt')
def read_event(request: Request):
    headers = request.headers
    for key, value in headers.items():
        print(f"{key}:{value}")
    
    return 'Hello from event route'
