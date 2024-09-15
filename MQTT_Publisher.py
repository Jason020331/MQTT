##Publisher (Sending data to MQTT Broker)

import paho.mqtt.client as mqtt
import Adafruit_DHT
import time
import json

# MQTT Broker details
broker_address = "b68048b371b3419485bc6600684525a8.s1.eu.hivemq.cloud"  # Replace with your HiveMQ Cloud broker address
port = 8883  # TLS Port for HiveMQ Cloud
username = "PnSIOT"  # Replace with your HiveMQ Cloud username
password = "Zhaode#123"  # Replace with your HiveMQ Cloud password
topic = "home/sensor/dht22"  # Topic to publish data

# Create a new MQTT client instance
client = mqtt.Client()

# Set username and password for HiveMQ Cloud authentication
client.username_pw_set(username, password)

# Use TLS for secure connection
client.tls_set()

# Connect to the broker
client.connect(broker_address, port)

# DHT22 sensor
sensor = Adafruit_DHT.DHT22
pin = 20  # GPIO Pin where the sensor is connected (e.g., GPIO 4)

# Publish sensor data every 5 seconds
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        # Prepare data in JSON format
        data = {
            "temperature": round(temperature, 1),
            "humidity": round(humidity, 1)
        }
        # Convert dictionary to JSON string
        data_out = json.dumps(data)
        
        # Publish the data to the MQTT broker
        client.publish(topic, data_out)
        print("Published {} to topic {}".format(data_out,topic))
    else:
        print("Failed to retrieve data from sensor")

    time.sleep(30)  # Send data every 5 seconds