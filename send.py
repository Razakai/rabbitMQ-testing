import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.queue_declare(queue='baka')



channel.basic_publish(exchange='',
                      routing_key='baka',
                      body='Hello World!')

print(" [x] Sent 'Hello World!'")

connection.close()