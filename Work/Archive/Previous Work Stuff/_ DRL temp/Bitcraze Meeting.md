Base station has a motion sensor within it that will turn off the laser.
- 

Mechanism for uploading base station geometry
- using a memory mapping 
- Feature and protocol in the library
- Not a high-speed thing

- Uploading geometry is given to persistent memory
	- Flash memory may be overwritten
	- Key value store
	- Can only be erased in pages
	- Done through python library
		- Memory mapping part

- Sensor positions
	- The yaw estimation will not work
	- Most of it is done outside of the Kalman estimator, in a pre-processor step
	- The assumption is still going to hold


Good first step:

Remove yaw estimation
- Makes it only use IMU
- Writing the lighthouse geometry
- There's a pointer for this, 

Libsurvive
- Open source VR
- There was some effort to reverse engineer the base stations

Kalman filter is *sensitive* to new 
- Standard deviation is low for the lighthouse.

# Debugging strategies
- Debugger

Use logging subsystem for graphing
- A system for setting up subscriptions for variables within the code
- Sent in real-time to the client. Easy to add your own logging variables if you want to see something.
	- It's possible to run the estimator within the PC as well

We'll likely want to increase the standard deviation on the Kalman filter
- Acceptance of errors should go up