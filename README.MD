# Track-O-Tron
Semester Long Design Project for NYU Tandon EG-1003

## Requirements
- [PlatformIO](https://platformio.org/platformio-ide) for compiling the Arduino code
- CMake for compiling the PC code

## Building
### PlatformIO (Arduino)
Enter the platformio/ subdirectory and open it in your PlatformIO IDE of choice, or build it using the PlatformIO CLI.

## Wiring
![Wiring Diagram](platformio/wiring-schematic/wiring-schematic.svg)
Connect each IMU's SPI pins to the hardware SPI pins on your microcontroller (pins 50, 51, and 52 for the Arduino Mega pictured above), and connect the accelerometer and magnetometer Chip Select (CS) pins to any digital pins. 
See [Adafruit's LSM9DS1 documentation](https://learn.adafruit.com/adafruit-lsm9ds1-accelerometer-plus-gyro-plus-magnetometer-9-dof-breakout/pinouts#spi-pins-2197900-7) for details.
Make sure to update the [LSM array in the platformIO main.cpp file](platformio/src/main.cpp#L19) to match which CS pins you are using! 
