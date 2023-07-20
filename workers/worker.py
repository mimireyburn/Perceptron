from confluent_kafka import Consumer, KafkaException
import psycopg2
import json

# Set up a Kafka consumer
c = Consumer({
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

# Subscribe to the Kafka topic
c.subscribe(['mytopic_sessionrecorder'])

# Database connection parameters
connection_info = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "host": "db",
    "port": 5432
}

while True:
    try:
        msg = c.poll(1.0)  # Timeout set to 1 second

        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())
        else:
            # Proper message
            print('Received message: {}'.format(msg.value().decode('utf-8')))

            # Here, you can add the code to process the message and insert it into the database.
            conn = psycopg2.connect(**connection_info)
            cur = conn.cursor()

            # Assuming the message.value() contains a JSON string like '{"userid": "abc", "session": "123"}'
            data = json.loads(msg.value().decode('utf-8'))  # decode the byte data to string
            userid = data.get('userid')
            session = data.get('session')
            datetime = data.get('datetime')

            # SQL Query to insert the data
            query = '''INSERT INTO sessions (user_id, item_key, cur_access) VALUES (%s, %s, %s);'''
            cur.execute(query, (userid, session, datetime))

            conn.commit()
            cur.close()
            conn.close()

    except KeyboardInterrupt:
        break
    except Exception as e:
        print(str(e))

c.close()
