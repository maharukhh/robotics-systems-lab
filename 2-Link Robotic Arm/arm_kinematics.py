"""
2-Link Robotic Arm — Forward & Inverse Kinematics
==============================================
Computes both directions of the kinematics problem for a planar 2-link
arm: forward kinematics (joint angles -> end-effector position) and
inverse kinematics (target position -> joint angles, via closed-form
trigonometric solution). Also sweeps the arm's full reachable workspace.
Companion piece to the "Robot Arm Joint-Angle" web simulator in this repo.

Usage
-----
    python arm_kinematics.py --task fk
    python arm_kinematics.py --task ik
    python arm_kinematics.py --task workspace
"""

import argparse

import matplotlib.pyplot as plt
import numpy as np


L1, L2 = 4.0, 3.0  # link lengths


def forward_kinematics(theta1, theta2):
    """theta1, theta2 in radians. Returns (elbow_xy, end_effector_xy)."""
    elbow = np.array([L1 * np.cos(theta1), L1 * np.sin(theta1)])
    end_effector = elbow + np.array([L2 * np.cos(theta1 + theta2), L2 * np.sin(theta1 + theta2)])
    return elbow, end_effector


def inverse_kinematics(x, y, elbow_up=True):
    """
    Closed-form 2-link IK. Returns (theta1, theta2) in radians, or None if
    the target is outside the arm's reach.
    """
    r = np.hypot(x, y)
    if r > (L1 + L2) or r < abs(L1 - L2):
        return None  # unreachable

    cos_theta2 = (r ** 2 - L1 ** 2 - L2 ** 2) / (2 * L1 * L2)
    cos_theta2 = np.clip(cos_theta2, -1, 1)
    theta2 = np.arccos(cos_theta2)
    if elbow_up:
        theta2 = -theta2

    k1 = L1 + L2 * np.cos(theta2)
    k2 = L2 * np.sin(theta2)
    theta1 = np.arctan2(y, x) - np.arctan2(k2, k1)
    return theta1, theta2


def plot_arm(ax, theta1, theta2, color="steelblue", label=None):
    elbow, end_effector = forward_kinematics(theta1, theta2)
    ax.plot([0, elbow[0], end_effector[0]], [0, elbow[1], end_effector[1]],
            marker="o", linewidth=3, color=color, label=label)
    return end_effector


def demo_fk():
    fig, ax = plt.subplots(figsize=(6, 6))
    angles = [(np.deg2rad(30), np.deg2rad(45)), (np.deg2rad(90), np.deg2rad(-30)), (np.deg2rad(150), np.deg2rad(60))]
    colors = ["steelblue", "crimson", "seagreen"]
    for (t1, t2), c in zip(angles, colors):
        ee = plot_arm(ax, t1, t2, color=c, label=f"θ1={np.rad2deg(t1):.0f}°, θ2={np.rad2deg(t2):.0f}°")
        print(f"θ1={np.rad2deg(t1):.0f}°, θ2={np.rad2deg(t2):.0f}° -> end-effector at ({ee[0]:.2f}, {ee[1]:.2f})")
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_aspect("equal")
    ax.legend(fontsize=8)
    ax.set_title("Forward Kinematics — Multiple Joint Configurations")
    ax.grid(alpha=0.3)
    plt.savefig("arm_fk.png", dpi=120)
    print("Saved visualization to arm_fk.png")
    plt.show()


def demo_ik():
    targets = [(5, 3), (-4, 4), (6, -1)]
    fig, ax = plt.subplots(figsize=(6, 6))
    colors = ["steelblue", "crimson", "seagreen"]
    for (x, y), c in zip(targets, colors):
        result = inverse_kinematics(x, y)
        if result is None:
            print(f"Target ({x}, {y}) is unreachable.")
            continue
        theta1, theta2 = result
        ee = plot_arm(ax, theta1, theta2, color=c, label=f"target ({x},{y})")
        ax.scatter(x, y, color=c, marker="x", s=100, zorder=5)
        print(f"Target ({x}, {y}) -> theta1={np.rad2deg(theta1):.1f}°, theta2={np.rad2deg(theta2):.1f}°, "
              f"reached ({ee[0]:.2f}, {ee[1]:.2f})")
    ax.set_xlim(-8, 8)
    ax.set_ylim(-8, 8)
    ax.set_aspect("equal")
    ax.legend(fontsize=8)
    ax.set_title("Inverse Kinematics — Solving for Target Positions")
    ax.grid(alpha=0.3)
    plt.savefig("arm_ik.png", dpi=120)
    print("Saved visualization to arm_ik.png")
    plt.show()


def demo_workspace():
    theta1_range = np.linspace(0, 2 * np.pi, 100)
    theta2_range = np.linspace(-np.pi, np.pi, 100)
    points = []
    for t1 in theta1_range:
        for t2 in theta2_range:
            _, ee = forward_kinematics(t1, t2)
            points.append(ee)
    points = np.array(points)

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.scatter(points[:, 0], points[:, 1], s=1, alpha=0.3, color="steelblue")
    ax.set_title(f"Reachable Workspace (L1={L1}, L2={L2})")
    ax.set_aspect("equal")
    ax.grid(alpha=0.3)
    plt.savefig("arm_workspace.png", dpi=120)
    print(f"Sampled {len(points)} reachable points across the joint space.")
    print("Saved visualization to arm_workspace.png")
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="2-link arm kinematics demos")
    parser.add_argument("--task", choices=["fk", "ik", "workspace"], required=True)
    args = parser.parse_args()
    {"fk": demo_fk, "ik": demo_ik, "workspace": demo_workspace}[args.task]()


if __name__ == "__main__":
    main()
