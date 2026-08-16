# Bang-Bang vs PID Control

A Python-based control systems project that compares **Bang-Bang (On-Off) Control** with **PID Control** using the same first-order plant.

## Features

* **Bang-Bang Control** — Simple ON/OFF feedback based on the error.
* **PID Control** — Uses proportional, integral, and derivative terms for smoother control.
* **Performance Comparison** — Compares both controllers under identical conditions.
* **Visualization** — Plots the system response and highlights the difference in stability and convergence.
* **Steady-State Analysis** — Calculates the output standard deviation for both controllers.

## Run

The program compares both controllers and saves the result as:

bang_bang_vs_pid.png

## how It Works

**Bang-Bang Control** switches the actuator fully ON or OFF depending on whether the system is below or above the setpoint. This makes it simple but can cause continuous oscillation around the target.

**PID Control** adjusts the correction according to the current error, accumulated error, and rate of change, allowing the system to approach the setpoint more smoothly.

## Dependencies


* Python 3.x
* NumPy
* Matplotlib

## key Concepts

This project demonstrates **feedback control, PID controllers, setpoint tracking, system response, steady-state error, and controller performance comparison**.
