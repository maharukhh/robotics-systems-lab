# Robotics & Intelligent Systems Applications

Two core building blocks of an autonomous mobile robot's navigation
stack, each demonstrated standalone with visualization: A* path planning
over an occupancy grid, and a PID controller tracking a waypoint path.

## 1. A* path planning (`--task path_planning`)
Plans a shortest path from start to goal across a 30×30 occupancy grid
seeded with randomly-placed rectangular obstacles, using 8-connected
movement (diagonal moves allowed, correctly costed at `√2` instead of
`1`) and a Euclidean heuristic. Saves a visualization (`astar_path.png`)
showing the grid, obstacles, and the resulting path from start to goal.

## 2. PID heading control (`--task pid_control`)
Simulates a **unicycle-model** robot (x, y, heading) driving at constant
linear velocity through a sequence of waypoints. A PID controller acts on
heading error at each timestep to compute an angular velocity command,
steering the robot toward the current waypoint before advancing to the
next — the same control structure used to steer a real differential-drive
robot along a planned path. Saves a trajectory visualization
(`pid_tracking.png`) plotting the robot's path against the waypoints.

## Why these two
Together they cover the **plan → control** half of the classic
sense-plan-act robotics loop: A* decides *where* to go, PID decides *how*
to get there smoothly. Both are implemented from first principles (no
planning/control libraries) to show the underlying logic rather than
just calling one.

## Tech stack
`numpy`, `matplotlib`

## Setup

## Usage

```bash
python robotics_applications.py --task path_planning
python robotics_applications.py --task pid_control
```

## Possible extensions
- Swap A* for RRT*/Hybrid-A* for kinodynamically-feasible planning
- Add obstacle-avoidance re-planning (re-run A* when the grid changes
  mid-traversal)
- Extend the PID heading controller to a full path-tracking controller
  (Pure Pursuit or Stanley controller) for smoother curvature tracking
- Wire both pieces into an actual ROS2 node (`/odom`, `/costmap` in,
  `/cmd_vel` out) to run against a real robot or Gazebo/Nav2 simulation
