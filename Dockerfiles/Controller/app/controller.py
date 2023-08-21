import time
import os
import pika

hostname = os.getenv('HOSTNAME')
print(hostname)
interval = int(os.getenv('EVENT_INTERVAL'))
print(interval)
RABBIT_MQ = os.getenv('RABBITMQ')
print(RABBIT_MQ)
RABBIT_MQ_PASSWORD = os.getenv('RABBITPASS')
print(RABBIT_MQ_PASSWORD)
OUTPUT_QUEUE = os.getenv('OUTPUT_QUEUE')
print(OUTPUT_QUEUE)
RABBIT_MQ_USERNAME = "user"  # Use the default "user" account
credentials = pika.PlainCredentials(RABBIT_MQ_USERNAME, RABBIT_MQ_PASSWORD)
parameters = pika.ConnectionParameters(host=RABBIT_MQ, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue=OUTPUT_QUEUE)

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    msg = "{\"data\": [ {\"msg\":\""+result+"\", \"hostname\": \""+hostname+"\"}]}"
    channel.basic_publish(exchange='', routing_key=OUTPUT_QUEUE, body=msg)
    print(result)
    time.sleep(interval)

connection.close()

