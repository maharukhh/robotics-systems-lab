# Robotics Systems Lab

A multi-stack collection of robotics and intelligent-systems projects — spanning path-planning and control algorithms in Python, and interactive front-end simulators built with vanilla HTML/CSS/JS. Built while studying Mechatronics, Robotics & Automation Engineering, this repo bridges algorithmic robotics work with hands-on, browser-based visualization of the same core concepts.

## Overview

Robotics work spans multiple layers — the algorithms that plan and control a robot's behavior, and the tools used to visualize, tune, and understand that behavior. This repo reflects that range on purpose: `python/` holds standalone algorithmic implementations (planning, control theory), while `web-simulators/` holds interactive, framework-free browser tools that make those same concepts (kinematics, PID tuning, sensor/actuator behavior) tangible without needing physical hardware or a full robotics framework like ROS.

## Projects

### Python — Algorithms & Control

| Project | Key Concepts |
|---|---|
| [Robotics & Intelligent Systems Applications] | A* path planning, PID path tracking, robot motion |
| [2-Link Robotic Arm] | Forward kinematics, inverse kinematics, workspace analysis |
| [Bang-Bang vs PID Control] | Feedback control, PID, on-off control, system response |
| [Boids Flocking Simulation] | Swarm robotics, multi-agent systems, emergent behavior |


### Web Simulators — Interactive Visualization

| Project | Key Concepts |
|---|---|
| [Robot Arm Joint-Angle] | SVG rendering, joint angles, forward kinematics |
| [Robot Movement Simulator (Grid)] | Keyboard controls, 2D coordinates, robot movement |
| [Line-Following Robot Path Simulator] | Path modeling, sensor-following logic |
| [Servo Motor Angle Control Simulator] | Slider controls, servo angles, SVG animation |
| [Motor Speed Control UI] | PWM, duty cycle, motor speed simulation |
| [Basic PID Controller Visualizer] | PID tuning, first-order plant, response visualization |
| [Sensor Threshold Alert UI] | Ultrasonic sensor simulation, threshold alerts, live gauge |


## Tech Stack

**Python:** NumPy, Matplotlib  
**Web:** HTML5, CSS3, JavaScript (ES6+)  
**Robotics Concepts:** A* Search, PID Control, Forward & Inverse Kinematics, Motion Planning, Flocking Algorithms, Sensor Simulation, Motor/Servo Control, Feedback Systems

## Repository Structure

```text
robotics-systems-lab/
├── Robotics & Intelligent Systems Applications/
├── 2-Link Robotic Arm/
├── Bang-Bang vs PID Control/
├── Boids Flocking Simulation/
├── Basic PID Controller Visualizer/
├── Robot Arm Joint-Angle/
├── Robot Movement Simulator (Grid)/
├── Line-Following Robot Path Simulator/
├── Servo Motor Angle Control Simulator/
├── Motor Speed Control UI/
├── Sensor Threshold Alert UI/
└── README.md
```

## Purpose

This repo consolidates robotics coursework and self-driven projects into one place — showing both the algorithmic foundations (search, control theory) and the ability to build clear, interactive tools around them. It's intended as a working portfolio: a single, coherent view of robotics-domain work across the stacks it actually gets built in.

## Status

🟢 Active — new algorithms and simulators added regularly.

## Author

**Mahrukh** — Robotics and Intelligent Systems Student
