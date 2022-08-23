# rpi-pico-watering-system

## Circuit diagram

![circuit diagram](doc/pico-w.drawio.png "circuit diagram")

## Data flow

![data flow](doc/data-flow.drawio.png "data flow")

## TODO
### hardware
- [x] make a first version of the circuit only with the rpi pico and wifi board for mqtt testing
- [ ] put everything together inside an electronics box
- [ ] connect the water tubes circuit
### software
- [x] figure out data flow between rpi pico and homeassistant with mqtt broker
- [x] create data model for mqtt topics
- [x] figure out how homeassistant can read data from mqtt and set thresholds for soil moisture and trigger a publish to relay topic that opens the relay for the specific sensor
- [x] create micro python script for rpi pico that connects to local wifi and sends to mqtt topics the sensors data
