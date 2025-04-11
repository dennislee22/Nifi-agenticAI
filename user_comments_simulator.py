from kafka import KafkaProducer
import json
import random
import time
from datetime import datetime

KAFKA_BROKER = 'my-cluster-kafka-bootstrap.dlee-kafkanodepool.svc.cluster.local:9092'
KAFKA_TOPIC = 'malay-comments'

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

messages = [
    {"text": "kamu sangat comel"},
    {"text": "saya tak comel"}
]

def stream_transactions():
    try:
        while True:
            message = random.choice(messages)
            producer.send(KAFKA_TOPIC, value=message)
            print(f"Sent message: {message}")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Producer stopped.")
    finally:
        producer.close()

if __name__ == '__main__':
    stream_transactions()
