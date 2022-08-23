import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

try:
    from secrets import secrets
except ImportError:
    print("Error, secrets could not be read")
    raise

mqtt_server = secrets['broker']
client_id = '1234123'

led = Pin("LED", Pin.OUT)
# temp = DHT11(Pin(17, Pin.OUT, Pin.PULL_DOWN))

sensor1 = Pin(11, Pin.IN)
sensor2 = Pin(12, Pin.IN)
sensor3 = Pin(13, Pin.IN)

relay1 = Pin(21, Pin.OUT, value=1)
relay2 = Pin(20, Pin.OUT, value=1)
relay3 = Pin(19, Pin.OUT, value=1)
relay4 = Pin(18, Pin.OUT, value=1)

last_sensor_reading = 0
readings_interval = 5

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets['ssid'], secrets['wifi_pass'])

while wlan.isconnected() == False:
  pass

time.sleep(5)

print("Connection successful")
print(wlan.ifconfig())


def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.set_callback(sub_cb)
    client.connect()
    for topic in secrets['sub_topics']:        
        client.subscribe(bytes(topic,'utf-8'))

    print("Connected to %s MQTT Broker" % (mqtt_server))
    return client


def reconnect():
    print("Failed to connect to the MQTT Broker. Reconnecting...")
    time.sleep(5)
    print('reconnect')
    machine.reset()


def sub_cb(topic, message):

    message = message.decode("utf-8")
    topic = topic.decode("utf-8")

    print("New message on topic {}".format(topic))
    print(message)

    if topic == "relays/relay1":
        if message == "on":
            relay1.value(0)
        else:
            relay1.value(1)
    if topic == "relays/relay2":
        if message == "on":
            relay2.value(0)
        else:
            relay2.value(1)
    if topic == "relays/relay3":
        if message == "on":
            relay3.value(0)
        else:
            relay3.value(1)
    if topic == "pump":
        if message == "on":
            relay4.value(0)
        else:
            relay4.value(1)


try:
    client = mqtt_connect()
except OSError as e:
    print('exception')
    reconnect()
    
while True:
    try:
        client.check_msg()

        if (time.time() - last_sensor_reading) > readings_interval:

            if sensor1.value() == 0:
                print("plant 1 needs water")
                client.publish(b"moisture/sensor1", b"on")
            else:
                print("plant 1 has enough water")
                client.publish(b"moisture/sensor1", b"off")
            if sensor2.value() == 0:
                print("plant 2 needs water")
                client.publish(b"moisture/sensor2", b"on")
            else:
                print("plant 2 has enough water")
                client.publish(b"moisture/sensor2", b"off")
            if sensor3.value() == 0:
                print("plant 3 needs water")
                client.publish(b"moisture/sensor3", b"on")
            else:
                print("plant 3 has enough water")
                client.publish(b"moisture/sensor3", b"off")
            last_sensor_reading = time.time()
    except OSError as e:
        reconnect()


