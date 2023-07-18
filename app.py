from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
import json

class Data(BaseModel):
    some_field: str  

@app.post('/')
async def read_root(request: Request):
    data = await request.json()
    print("hi this is a log")
    print(data)
    return {'Hello': 'Docker with FastAPI!'}

@app.get('/')
async def read_root(request: Request):
    data = await request.json()
    print("hi this is a log")
    print(data)
    return {'Hello': 'Docker with FastAPI!'}

@app.post('/evt')
def read_root(data: Data):
    print(data.some_field)
    return {'Hello': 'Docker with FastAPI!', 'Your Data': data.some_field}

@app.get('/evt')
def read_event(data):
    print("hi this is a log")
    print(data)
    return {'Hello': 'welcome to the event endpoint'}