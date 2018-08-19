# Estimation Project #
![All That I Do](./images/Logo.PNG)

In this project, we will be developing an estimator to be used by your controller to successfully fly a desired flight path using realistic sensors. 

### Step 1: Sensor Noise ###
#### Determine the standard deviation of the measurement noise of both GPS X data and Accelerometer X data. ####
The calculated standard deviation should correctly capture ~68% of the sensor measurements. Your writeup should describe the method used for determining the standard deviation given the simulated sensor measurements. 

- MeasuredStdDev_GPSPosXY = 0.67
- MeasuredStdDev_AccelXY = .49
- [Standard deviation calculator](sensorNoise/SensorNoise.py)
 ----
### Step 2: Attitude Estimation ###
#### Implement a better rate gyro attitude integration scheme in the UpdateFromIMU() function. ####
The improved integration scheme should result in an attitude estimator of < 0.1 rad for each of the Euler angles for a duration of at least 3 seconds during the simulation. The integration scheme should use quaternions to improve performance over the current simple integration scheme. 

- changes are reflected in [src/QuadEstimatorEKF.cpp#L103-L124](src/QuadEstimatorEKF.cpp#L103-L124)

 ----
### Step 3: Prediction Step ###
#### Implement all of the elements of the prediction step for the estimator. ####
The prediction step should include the state update element (PredictState() function), a correct calculation of the Rgb prime matrix, and a proper update of the state covariance. The acceleration should be accounted for as a command in the calculation of gPrime. The covariance update should follow the classic EKF update equation. 

- changes are reflected for PredictState in [PredictState()#L179-L194](src/QuadEstimatorEKF.cpp#L179-L194)
- changes are reflected for GetRbgPrime in [GetRbgPrime()#L222-L234](src/QuadEstimatorEKF.cpp#L222-L234)
- changes are reflected for Predict/Covariance in [Predict()#L271-L291](src/QuadEstimatorEKF.cpp#L271-L291)

 ----
### Step 4: Magnetometer Update ###
#### Implement the magnetometer update. ####
The update should properly include the magnetometer data into the state. Note that the solution should make sure to correctly measure the angle error between the current state and the magnetometer value (error should be the short way around, not the long way). 

- changes are reflected in [src/QuadEstimatorEKF.cpp#L346-L360](src/QuadEstimatorEKF.cpp#L346-L360)

 ----
### Step 5: Closed Loop + GPS Update ###
#### Implement the GPS update. ####
The estimator should correctly incorporate the GPS information to update the current state estimate. 

- changes are reflected in [src/QuadEstimatorEKF.cpp#L315-L325](src/QuadEstimatorEKF.cpp#L315-L325)
- changes are reflected in [config/11_GPSUpdate.txt](config/11_GPSUpdate.txt)
- Quad.UseIdealEstimator = 0
- #SimIMU.AccelStd = 0,0,0
- #SimIMU.GyroStd = 0,0,0
