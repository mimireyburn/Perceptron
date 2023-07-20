from fastapi import FastAPI, Request, HTTPException
from confluent_kafka import Producer, Consumer
import redis
import random
import json
from datetime import datetime

app = FastAPI()

@app.get('/')
async def read_root(request: Request):
    headers = request.headers
    userid = headers.get('user')
    session = headers.get('session')

    r = redis.Redis(host='cache', port=6379, decode_responses=True)
    r.zadd('recommendations', {'ee34f214-bea6-4cde-bb46-cf5db7eb05a8': 0.8, '6e7175d0-1abd-496f-a138-d447b220b8b6': 0.7, '43a2a257-dd0c-4a6a-8b2b-457b443eb1cb': 0.6, '9f60e2f8-7f11-4732-a69a-03d2ea6e2950': 0.4})


    # Get the current datetime
    current_datetime = datetime.now().isoformat()

    r.set(f"user:{userid}", userid)
    r.set(f"session:{session}", session)
    r.set(f"datetime:{current_datetime}", current_datetime)
    
    user_recommendations = r.zrange('recommendations', 0, -1, withscores=True)

    selected_item, score = random.choice(user_recommendations)


    # Kafka producer
    p = Producer({'bootstrap.servers': 'kafka:9092'})

    # Create a dictionary to hold the data
    data = {
        'userid': userid,
        'session': session,
        'datetime': current_datetime
    }

    # Convert the dictionary to a JSON string
    data_str = json.dumps(data)

    p.produce('mytopic_sessionrecorder', key=userid, value=data_str, callback=delivery_report)
    p.flush()
    
    return selected_item


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

@app.post('/evt')
def read_event(request: Request):
    headers = request.headers
    for key, value in headers.items():
        print(f"{key}:{value}")
    
    return 'Hello from event route'