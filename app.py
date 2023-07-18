from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root(data):
    print(data)
    return {'Hello': 'Docker with FastAPI!'}

@app.get('/evt')
def read_event(data):
    print(data)
    return {'Hello': 'Docker with FastAPI!'}