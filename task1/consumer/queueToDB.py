import pika
from pymongo import MongoClient


connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task1')

dbConnection = MongoClient(host='mongodb', port=27017)
db = dbConnection.testDB
collection = db.testCollection

print('Waiting for messages...')

def callback(ch, method, properties, body):
    print(body)
    collection.insert({"string": body})


channel.basic_consume(callback, queue='task1', no_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
    print('\nreceiving is completed')