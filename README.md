# rpi-pico-watering-system
## TODO
- hardware
  - make a first version of the circuit only with the rpi pico and wifi board for mqtt testing
- software
  - figure out data flow between rpi pico and homeassistant with mqtt broker
  - create data model for mqtt topics
  - figure out how homeassistant can read data from mqtt and set thresholds for soil moisture and trigger a publish to relay topic that opens the relay for the specific sensor
