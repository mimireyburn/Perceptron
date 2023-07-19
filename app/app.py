from fastapi import FastAPI, Request, HTTPException
import redis
import random
import pg8000
import json

app = FastAPI()

r = redis.Redis(host='cache', port=6379, decode_responses=True)
r.zadd('recommendations:user:1', {'ee34f214-bea6-4cde-bb46-cf5db7eb05a8': 0.8, '6e7175d0-1abd-496f-a138-d447b220b8b6': 0.7, '43a2a257-dd0c-4a6a-8b2b-457b443eb1cb': 0.6}, {'9f60e2f8-7f11-4732-a69a-03d2ea6e2950', 0.4})

@app.get('/')
async def read_root(request: Request):
    headers = request.headers
    userid = headers.get('user')
    session = headers.get('session')

    r.set(f"user:{userid}", session)

    user_recommendations = r.zrange('recommendations:user:1', 0, -1, withscores=True)

    selected_item, score = random.choice(user_recommendations)
    
    return selected_item

@app.post('/evt')
def read_event(request: Request):
    headers = request.headers
    for key, value in headers.items():
        print(f"{key}:{value}")
    
    return 'Hello from event route'


# connection_info = {
    # "database": "postgres",
    # "user": "postgres",
    # "password": "Perceptron",
    # "host": "localhost",
    # "port": 5433  # or any port you have configured
    # }
    
    # if userid is None or session is None:
    #     raise HTTPException(status_code=400, detail="Missing user or session in headers")


    # def item_returner(connection_info, userid):
    #     conn = pg8000.connect(**connection_info)
    #     cur = conn.cursor()

    #     cur.execute(
    #         """
    #         SELECT item_key FROM items WHERE user_id = %s
    #         """,
    #         (userid,)  # Notice the comma, making it a tuple
    #     )
    #     item_keys = cur.fetchall()

    #     cur.close()
    #     conn.close()

    #     return item_keys

    # item = item_returner(connection_info, userid)

    # user_data = r.hgetall(f'user-session:{session}')
