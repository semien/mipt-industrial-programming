import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='0.0.0.0', port=5672))
channel = connection.channel()
channel.queue_declare(queue='task1')

print("Start sending...")

try:
    while True:
        line = input("message> ")
        channel.basic_publish(exchange='', routing_key='task1', body=line)
except KeyboardInterrupt:
    print('\ninput is completed')