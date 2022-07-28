from machine import ADC, Pin
from utime import sleep 

pot = ADC(26)

maxValue=65535
minValue=26000

def convert_to_percent(value):
    
    percent = 100 - (value-minValue)/(maxValue-minValue) * 100
    return percent
    

while True:
     raw = pot.read_u16()
     print('Raw: {} '.format(raw))
     print(str(convert_to_percent(raw)) + "%")
     sleep(1)
