#!/usr/bin/env python3
import asyncio
import subprocess

import accel
#import imu
import net

# Get the IP address of this Raspberry Pi
host = (
    subprocess.run(["hostname", "-I"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

# Port 10030 for EG-1003
port = 10030

# Setup the sensor, either a MMA8451 or LSM9DS1 module from Adafruit
# sensor = imu.LSM()
sensor = accel.MMA()

# Setup networking sockets for sending IMU data to the PC
data_server = net.DataServer(host, port, sensor.getData)

asyncio.run(data_server.run_server())
