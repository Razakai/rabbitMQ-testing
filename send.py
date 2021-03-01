import pika
import json
import numpy as np
import cv2
from PIL import Image

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='testingDetection')
channel.queue_declare(queue='hello')
channel.queue_declare(queue='baka')
channel.queue_declare(queue='baka2')


image = Image.open('65.jpg').convert('RGB')
image = np.array(image)
image = cv2.resize(image, (200, 50), interpolation=cv2.INTER_AREA)

image = (cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) / 127.5) - 1.0
image = [image.tolist()]




channel.basic_publish(exchange='',
                      routing_key='baka2',
                      body=json.dumps({"detections": str(image), "city": "Cork", "country": "Ireland"}))
                    

print(" [x] Sent message")

connection.close()