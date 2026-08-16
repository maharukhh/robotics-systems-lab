# Sensor Threshold Alert UI (Mock Ultrasonic Sensor)

A browser-based interactive sensor monitoring interface that simulates an ultrasonic distance sensor using a circular gauge and a pulsing alert banner. The system triggers an alert when a simulated object moves closer than an adjustable distance threshold and logs each alert/clear state transition with a timestamp.

## Run it

Open `index.html` in a modern web browser.

## Concepts demonstrated

* Threshold-based alerting logic that logs only **state transitions**, rather than every sensor reading
* Adjustable distance threshold for triggering alerts
* CSS `conic-gradient` used to create a live circular sensor gauge
* Simple randomized sensor data simulation
* Real-time visual feedback for sensor state changes
* Timestamped alert and clear event logging

## Next steps

Add an audible alert using the Web Audio API and implement a configurable **hysteresis band** to reduce alert flickering when the sensor value fluctuates near the threshold.
