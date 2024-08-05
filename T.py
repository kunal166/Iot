# Import the Adafruit_DHT library for reading from DHT11/DHT22 sensors
import Adafruit_DHT

# Import the paho.mqtt.client library for MQTT communication
import paho.mqtt.client as mqtt

# Specify the type of sensor being used (DHT11) and the GPIO pin it's connected to
sensor = Adafruit_DHT.DHT11
pin = 4

# Define a function to read the sensor data
def read_sensor():
    # Read the humidity and temperature from the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    return humidity, temperature

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker (in this case, a public broker at hivemq.com)
client.connect("broker.hivemq.com", 1883, 60)

# Read the humidity and temperature from the sensor
humidity, temperature = read_sensor()

# Publish the temperature data to the "home/temperature" topic
client.publish("home/temperature", temperature)

# Publish the humidity data to the "home/humidity" topic
client.publish("home/humidity", humidity) hai
