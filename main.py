from machine import ADC, Pin
from utime import sleep
import dht

sensor1 = Pin(22, Pin.IN)
sensor2 = Pin(26, Pin.IN)
sensor3 = Pin(27, Pin.IN)

relay1 = Pin(21, Pin.OUT, value=1)
relay2 = Pin(20, Pin.OUT, value=1)
relay3 = Pin(19, Pin.OUT, value=1)
relay4 = Pin(18, Pin.OUT, value=1)

tempSensor = dht.DHT11(Pin(15, Pin.IN))

while True:
    
     #try:
         #sleep(2)
         #tempSensor.measure()
         #temp = tempSensor.temperature()
         #hum = tempSensor.humidity()
         #print(temp)
         #print(hum)
     #except OSError as e:
         #print('Failed to read sensor.')
     
     if(sensor1.value() == 1):
         relay1.on()
         relay4.on()
     else:
         relay1.off()
         relay4.off()
         
     if(sensor2.value() == 1):
         relay1.on()
         relay3.on()
     else:
         relay1.off()
         relay3.off()
         
     if(sensor3.value() == 1):
         relay1.on()
         relay2.on()
     else:
         relay1.off()
         relay2.off()
