import adafruit_lsm9ds1
import board
import busio
from digitalio import DigitalInOut, Direction


class LSM:
    def __init__(self):
        # SPI connection: (TODO: Add support for multiple IMU modules)
        spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
        csag = DigitalInOut(board.D5)
        csag.direction = Direction.OUTPUT
        csag.value = True
        csm = DigitalInOut(board.D6)
        csm.direction = Direction.OUTPUT
        csm.value = True
        self.sensor = adafruit_lsm9ds1.LSM9DS1_SPI(spi, csag, csm)

    def getData(self):
        # Read acceleration, magnetometer, gyroscope, temperature.
        accel_x, accel_y, accel_z = self.sensor.acceleration
        mag_x, mag_y, mag_z = self.sensor.magnetic
        gyro_x, gyro_y, gyro_z = self.sensor.gyro
        # temp = sensor.temperature

        return (
            "Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
                accel_x, accel_y, accel_z
            )
            + "Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
                mag_x, mag_y, mag_z
            )
            + "Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})".format(
                gyro_x, gyro_y, gyro_z
            )
        )
