from fastapi import FastAPI, Request
import redis
from fastapi import FastAPI, Request, HTTPException
import psycopg2
import json

app = FastAPI()

@app.get('/')
async def read_root(request: Request):
    headers = request.headers
    for key, value in headers.items():
        print(f"{key}:{value}")
    r = redis.Redis(host='cache', port=6379, decode_responses=True)
    r.set("user",headers.get('user') )
    r.set("session", headers.get('session'))
    r.hset('user-session:123', mapping={
        'name': 'John',
        "surname": 'Smith',
        "company": 'Redis',
        "age": 29
    })

    r.hgetall('user-session:123')
    # {'surname': 'Smith', 'name': 'John', 'company': 'Redis', 'age': '29'}
    return '0007933c-e702-4ccf-872c-d5235d6ee51a'

@app.post('/evt')
def read_event(request: Request):
    headers = request.headers
    for key, value in headers.items():
        print(f"{key}:{value}")
        
    
    return 'Hello from event route'
