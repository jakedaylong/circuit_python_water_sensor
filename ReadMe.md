# Circuit Python Water Sensor 

This sensor was a school project inspired by a need to keep tabs on a growning garden. The first itteration is to simply get the monitor working and be able to wirelessly receive data from device without the use of WiFi.

Instead of WiFi a packet radio, listed below, is used to send a transmission of the current sensor state to the receiving system. This radio type was used for better control over power consumption for the transmitting device as the next enhancments to the hardware will include a battery and small solar panel.

This repository was developed along side this one: [python_plant_monitor_client](https://github.com/jakedaylong/python_plant_monitor_client).

These two repositories with remain more or less in sync with each other to allow easy loading to desired devices of a similar nature.

See requirements.txt for packages.

## Hardware Used
* Raspberry Pi Pico W
* Monk Makes Plant Monitor
* Adafruit RFM69HCW 915Mhz Packet Radio


## Future 
* Add battery, charger, and solar panel to sensor hardware
* Add support for battery state of charge monitoring
* Add support for multi-radio configuration to support sensors for every garden area
* Add support for PH reading of soil conditions