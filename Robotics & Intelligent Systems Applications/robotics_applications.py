"""
Robotics & Intelligent Systems Applications
==============================================
Two core building blocks of an autonomous mobile robot stack, each
runnable standalone:

  1. A* path planning over an occupancy grid
  2. A PID controller simulated against a simple robot dynamics model,
     tracking a path produced by (1)

Usage
-----
    python robotics_applications.py --task path_planning
    python robotics_applications.py --task pid_control
"""

import argparse
import heapq

import matplotlib.pyplot as plt
import numpy as np


# --------------------------------------------------------------------------
# 1. A* path planning over a 2D occupancy grid
# --------------------------------------------------------------------------
def heuristic(a, b):
    # Euclidean heuristic — admissible for 8-connected grid movement
    return np.hypot(a[0] - b[0], a[1] - b[1])


def astar(grid: np.ndarray, start: tuple, goal: tuple):
    """
    grid: 2D numpy array, 0 = free, 1 = obstacle.
    Returns the shortest path from start to goal as a list of (row, col)
    tuples, or None if unreachable.
    """
    neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    rows, cols = grid.shape

    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        for dr, dc in neighbors:
            neighbor = (current[0] + dr, current[1] + dc)
            if not (0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols):
                continue
            if grid[neighbor[0], neighbor[1]] == 1:
                continue

            step_cost = np.hypot(dr, dc)  # 1.0 for straight moves, ~1.41 for diagonal
            tentative_g = g_score[current] + step_cost

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current

    return None  # no path found


def demo_path_planning():
    rng = np.random.default_rng(7)
    grid = np.zeros((30, 30), dtype=int)

    # scatter some rectangular obstacles to make the planner do real work
    for _ in range(6):
        r, c = rng.integers(0, 25, size=2)
        h, w = rng.integers(3, 8, size=2)
        grid[r:r + h, c:c + w] = 1

    start, goal = (0, 0), (29, 29)
    grid[start], grid[goal] = 0, 0  # keep endpoints clear

    path = astar(grid, start, goal)
    if path is None:
        print("No path found.")
        return

    print(f"Path found with {len(path)} steps.")

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(grid, cmap="Greys")
    path_arr = np.array(path)
    ax.plot(path_arr[:, 1], path_arr[:, 0], color="red", linewidth=2, label="A* path")
    ax.scatter(*start[::-1], c="green", s=80, label="start")
    ax.scatter(*goal[::-1], c="blue", s=80, label="goal")
    ax.legend()
    ax.set_title("A* Path Planning on Occupancy Grid")
    plt.savefig("astar_path.png", dpi=120)
    print("Saved visualization to astar_path.png")
    plt.show()


# --------------------------------------------------------------------------
# 2. PID controller tracking a reference path (simple differential-drive
#    style kinematics: robot has position + heading, PID drives heading
#    error to zero to steer toward the next waypoint)
# --------------------------------------------------------------------------
class PIDController:
    def __init__(self, kp, ki, kd, dt):
        self.kp, self.ki, self.kd, self.dt = kp, ki, kd, dt
        self.integral = 0.0
        self.prev_error = 0.0

    def compute(self, error):
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative


def simulate_pid_path_tracking(waypoints, dt=0.1, v=1.0, kp=2.0, ki=0.0, kd=0.3, waypoint_radius=0.5):
    """
    Simulates a unicycle-model robot (x, y, theta) driving at constant
    linear velocity `v`, using a PID controller on heading error to steer
    toward each waypoint in sequence.
    """
    pid = PIDController(kp, ki, kd, dt)
    x, y, theta = waypoints[0][0], waypoints[0][1], 0.0
    trajectory = [(x, y)]

    for wp in waypoints[1:]:
        while np.hypot(wp[0] - x, wp[1] - y) > waypoint_radius:
            target_heading = np.arctan2(wp[1] - y, wp[0] - x)
            heading_error = np.arctan2(np.sin(target_heading - theta), np.cos(target_heading - theta))

            omega = pid.compute(heading_error)  # angular velocity command
            theta += omega * dt
            x += v * np.cos(theta) * dt
            y += v * np.sin(theta) * dt
            trajectory.append((x, y))

            if len(trajectory) > 20000:  # safety cutoff against a runaway sim
                break

    return np.array(trajectory)


def demo_pid_control():
    waypoints = [(0, 0), (5, 5), (10, 0), (15, 8), (20, 0)]
    trajectory = simulate_pid_path_tracking(waypoints)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(trajectory[:, 0], trajectory[:, 1], label="robot trajectory", linewidth=2)
    wp_arr = np.array(waypoints)
    ax.plot(wp_arr[:, 0], wp_arr[:, 1], "o--", color="gray", label="waypoints")
    ax.set_title("PID Heading Control Tracking a Waypoint Path")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.axis("equal")
    plt.savefig("pid_tracking.png", dpi=120)
    print("Saved visualization to pid_tracking.png")
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Robotics & intelligent systems demos")
    parser.add_argument("--task", choices=["path_planning", "pid_control"], required=True)
    args = parser.parse_args()

    if args.task == "path_planning":
        demo_path_planning()
    elif args.task == "pid_control":
        demo_pid_control()


if __name__ == "__main__":
    main()