import board
import busio

import adafruit_mma8451


class MMA:
    def __init__(self):
        # Initialize I2C bus.
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # Initialize MMA8451 module.
        self.sensor = adafruit_mma8451.MMA8451(self.i2c)
        # Optionally change the address if it's not the default:
        # sensor = adafruit_mma8451.MMA8451(i2c, address=0x1C)

        # Optionally change the range from its default of +/-4G:
        self.sensor.range = adafruit_mma8451.RANGE_2G  # +/- 2G
        # sensor.range = adafruit_mma8451.RANGE_4G  # +/- 4G (default)
        # sensor.range = adafruit_mma8451.RANGE_8G  # +/- 8G

        # Optionally change the data rate from its default of 800hz:
        # sensor.data_rate = adafruit_mma8451.DATARATE_800HZ  #  800Hz (default)

    def getData(self):
        x, y, z = self.sensor.acceleration
        orientation = self.sensor.orientation
        return "x={0:0.3f} y={1:0.3f} z={2:0.3f} ori={3}".format(x, y, z, orientation)

        # Orientation is one of these values:
        #  - PL_PUF: Portrait, up, front
        #  - PL_PUB: Portrait, up, back
        #  - PL_PDF: Portrait, down, front
        #  - PL_PDB: Portrait, down, back
        #  - PL_LRF: Landscape, right, front
        #  - PL_LRB: Landscape, right, back
        #  - PL_LLF: Landscape, left, front
        #  - PL_LLB: Landscape, left, back
        # print("Orientation: ", end="")
        # if orientation == adafruit_mma8451.PL_PUF:
        #     print("Portrait, up, front")
        # elif orientation == adafruit_mma8451.PL_PUB:
        #     print("Portrait, up, back")
        # elif orientation == adafruit_mma8451.PL_PDF:
        #     print("Portrait, down, front")
        # elif orientation == adafruit_mma8451.PL_PDB:
        #     print("Portrait, down, back")
        # elif orientation == adafruit_mma8451.PL_LRF:
        #     print("Landscape, right, front")
        # elif orientation == adafruit_mma8451.PL_LRB:
        #     print("Landscape, right, back")
        # elif orientation == adafruit_mma8451.PL_LLF:
        #     print("Landscape, left, front")
        # elif orientation == adafruit_mma8451.PL_LLB:
        #     print("Landscape, left, back")
