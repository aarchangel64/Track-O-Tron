/**
 *
 */
#include "Arduino.h"

#include <Adafruit_LSM9DS1.h>
#include <Adafruit_MMA8451.h>
#include <Adafruit_Sensor.h>
#include <SPI.h>
#include <Wire.h>

using LSM = Adafruit_LSM9DS1;
using Vec3 = LSM::lsm9ds1Vector_t;

// using LSM = Adafruit_MMA8451;

// Construct LSM objects for hardware SPI.
// CS pins (XGCS, MCS) are taken as parameters
LSM imus[] = {
    {28, 27}, // IMU 0, which could be e.g. forearm_r
    {30, 29}, // IMU 1, which could be e.g. forearm_l
    {32, 31}, // IMU 2
    {34, 33}, // IMU 3
    {36, 35}  // IMU 4
};

struct Data {
  Data(const LSM &imu)
      : accel{imu.accelData}, gyro{imu.gyroData}, mag{imu.magData} {};

  const Vec3 &accel;
  const Vec3 &gyro;
  const Vec3 &mag;
};

template <typename T> const inline size_t writeData(const T i) {
  return Serial.write(reinterpret_cast<const byte *>(&i), sizeof(T));
}

void setup() {
  Serial.begin(115200);

  // Wait for a serial connection to be opened
  while (!Serial) {
    delay(1);
  }
  // Check that all IMUs are detected
  for (auto &i : imus) {
    if (!i.begin()) {
      Serial.println("IMU not detected");
      while (true)
        delay(10);
    }

    // Set sensor ranges
    i.setupAccel(LSM::LSM9DS1_ACCELRANGE_2G);
    i.setupGyro(LSM::LSM9DS1_GYROSCALE_245DPS);
    i.setupMag(LSM::LSM9DS1_MAGGAIN_4GAUSS);

    // i.setRange(MMA8451_RANGE_2_G);
  }
}

void loop() {
  if (Serial.available() > 0 && Serial.read() == 'a') {
    Serial.flush();
    for (auto &i : imus) {
      // Update IMU readings
      i.readAccel();
      i.readGyro();
      i.readMag();

      // Construct a Data Struct containing raw IMU data
      const Data packet = Data{i};
      writeData<>(&packet);
    }
  }
  delay(300);
}
