import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='testingDetection')
channel.queue_declare(queue='hello')
channel.queue_declare(queue='baka')



channel.basic_publish(exchange='',
                      routing_key='testingDetection',
                      body=json.dumps({"message": "http://192.168.1.103:1234/video"}))
                      #body="http://192.168.1.103:1234/video")

print(" [x] Sent message")

connection.close()