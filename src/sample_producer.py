import datetime
import time
import json
import pika  # Python AMQP Library

RABBIT_HOST = "123.123.123.123"
RABBIT_USER = "guest"
# RABBIT_PWD_ENCRYPTED =
RABBIT_PWD_DECRYPTED = "guest"

credentials = pika.PlainCredentials(RABBIT_USER, RABBIT_PWD_DECRYPTED)

parameters = pika.ConnectionParameters(credentials=credentials, port=8082, host=RABBIT_HOST, virtual_host="/")


def lambda_handler(event, context):
    event = None
    with open("extractingTask.json", "r") as f:
        event = json.load(f)

    connection = pika.BlockingConnection(parameters)  # Establishes TCP Connection with RabbitMQ
    channel = connection.channel()  # Establishes logical channel within Connection
    for i in range(10):
        time.sleep(1)
        # Send Message
        channel.basic_publish(exchange='', routing_key='xxxx-transient', body=json.dumps(event))
        print("complete putting one event.")

    connection.close()  # Close Connection and Channel(s) within


if __name__ == '__main__':
    lambda_handler(None, None)
