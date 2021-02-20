import os
import pika
import sys
import json
import numpy as np

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='baka')

    def callback(ch, method, properties, body):
       # print(" [x] baka >~< Received", json.loads(body))
        array = eval(json.loads(body)["detections"])
        print("\n\n\n", np.asarray(array[0]), np.asarray(array[0]).shape)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue='baka', on_message_callback=callback)

    channel.basic_qos(prefetch_count=1)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)