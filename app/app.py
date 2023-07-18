from fastapi import FastAPI, Request

app = FastAPI()

@app.get('/')
async def read_root(request: Request):
    headers = request.headers
    for key, value in headers.items():
        print(f"{key}:{value}")
    return '0007933c-e702-4ccf-872c-d5235d6ee51a'

@app.post('/evt')
def read_event(request: Request):
    headers = request.headers
    for key, value in headers.items():
        print(f"{key}:{value}")
    return 'Hello from event route'