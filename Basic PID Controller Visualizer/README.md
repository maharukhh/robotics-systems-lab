# Basic PID Controller Visualizer

An interactive browser-based PID controller visualizer that allows users to adjust P, I, and D gains along with a target setpoint and observe how a simulated first-order plant (e.g., motor speed or temperature) responds over time. The project demonstrates key PID control behaviors such as overshoot, oscillation, response speed, and settling.

## Run it

Open `index.html` in a modern web browser.

## Concepts demonstrated

* The PID control law: `output = Kp*error + Ki*∫error + Kd*d(error)/dt`
* Adjustable P, I, and D gains for interactive controller tuning
* Discrete-time simulation of a first-order lag plant
* Setpoint tracking and system response analysis
* Canvas-based time-series plotting with a setpoint reference line
* Visualization of overshoot, oscillation, and settling behavior

## Next steps

Add a step-disturbance button to observe how the controller responds to external changes, or add a second trace to overlay an alternate gain set and compare different tuning choices side by side.
