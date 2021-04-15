#include "../include/attitudeConv.hpp"

AttitudeConverter::AttitudeConverter()
{
				// Initialise the estimator (e.g. in the class constructor, none of these are actually strictly required for the estimator to work, and can be set at any time)
				Est.setMagCalib(0.68, -1.32, 0.0);         // Recommended: Use if you want absolute yaw information as opposed to just relative yaw (Default: (1.0, 0.0, 0.0))
				Est.setPIGains(2.2, 2.65, 10, 1.25);       // Recommended: Use if the default gains (shown) do not provide optimal estimator performance (Note: Ki = Kp/Ti)
				Est.setQLTime(2.5);                        // Optional: Use if the default quick learning time is too fast or too slow for your application (Default: 3.0)
				Est.setAttitude(0.5, 0.5, 0.5, 0.5);       // Optional: Use if you have prior knowledge about the orientation of the robot (Default: Identity orientation)
				Est.setAttitudeEuler(M_PI, 0.0, 0.0);      // Optional: Use if you have prior knowledge about the orientation of the robot (Default: Identity orientation)
				Est.setAttitudeFused(M_PI, 0.0, 0.0, 1.0); // Optional: Use if you have prior knowledge about the orientation of the robot (Default: Identity orientation)
				Est.setGyroBias(0.152, 0.041, -0.079);     // Optional: Use if you have prior knowledge about the gyroscope bias (Default: (0.0, 0.0, 0.0))
}

std::unique_ptr<AttitudeConverter> new_converter()
{
				return std::make_unique<AttitudeConverter>();
}
