# Robotics Systems Lab

A multi-stack collection of robotics and intelligent-systems projects — spanning path-planning and control algorithms in Python, and interactive front-end simulators built with vanilla HTML/CSS/JS. Built while studying Mechatronics, Robotics & Automation Engineering, this repo bridges algorithmic robotics work with hands-on, browser-based visualization of the same core concepts.

## Overview

Robotics work spans multiple layers — the algorithms that plan and control a robot's behavior, and the tools used to visualize, tune, and understand that behavior. This repo reflects that range on purpose: `python/` holds standalone algorithmic implementations (planning, control theory), while `web-simulators/` holds interactive, framework-free browser tools that make those same concepts (kinematics, PID tuning, sensor/actuator behavior) tangible without needing physical hardware or a full robotics framework like ROS.

## Projects

### Python — Algorithms & Control

| Project | Key Concepts |
|---|---|
| ✅ [A\* Path Planning](python/robotics_applications.py) | Grid-based search, occupancy grids, heuristic pathfinding |
| ✅ [PID Path-Tracking Controller](python/robotics_applications.py) | Closed-loop control, unicycle-model kinematics, heading-error correction |

Both are runnable standalone via:
```bash
python robotics_applications.py --task path_planning
python robotics_applications.py --task pid_control
```
Each generates a saved visualization (`astar_path.png`, `pid_tracking.png`) and displays it interactively.

### Web Simulators — Interactive Visualization

| Project | Key Concepts |
|---|---|
| ✅ Robot Arm Joint-Angle Form | SVG rendering, form-to-visual binding, forward kinematics |
| ✅ Grid Movement Simulator | Keyboard event handling, 2D coordinate state |
| ✅ Line-Following Path Simulator | Path/track modeling, sensor-following logic |
| ✅ Servo Angle Control | Slider input, real-time SVG rotation |
| ✅ Motor PWM / Speed Control | Duty-cycle math, real-time UI feedback |
| ⬜ PID Controller Visualizer | Control theory, live response plotting |
| ⬜ Maze Solver Visualizer | BFS/DFS algorithms, step-through visualization |
| ⬜ Sensor Threshold Alert UI | Mock sensor streams, conditional alert logic |
| ⬜ Inverse Kinematics Solver | 2-link arm IK, trigonometric solving |
| ⬜ Obstacle Avoidance Simulator | Raycasting, reactive navigation |

*(✅ = completed and in the repo · ⬜ = planned)*

## Tech Stack

**Languages:** Python (NumPy, Matplotlib), HTML5, CSS3, JavaScript (ES6+)
**Concepts:** A\* Search, PID / Control Theory, Forward & Inverse Kinematics, Finite State Machines, Sensor/Actuator Simulation, SVG/Canvas Rendering, Event-Driven Programming

## Repository Structure

```
robotics-systems-lab/
├── python/
│   └── robotics_applications.py     # A* planning + PID control demos
├── web-simulators/
│   ├── robot-arm-joint-angle/
│   ├── grid-movement-simulator/
│   ├── line-following-path-simulator/
│   ├── servo-angle-control/
│   └── motor-pwm-control/
└── README.md
```

## Purpose

This repo consolidates robotics coursework and self-driven projects into one place — showing both the algorithmic foundations (search, control theory) and the ability to build clear, interactive tools around them. It's intended as a working portfolio: a single, coherent view of robotics-domain work across the stacks it actually gets built in.

## Status

🟢 Active — new algorithms and simulators added regularly.

## Author

**Mahrukh** — Robotics and Intelligent Systems Student
