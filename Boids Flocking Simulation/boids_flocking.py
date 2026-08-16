"""
Boids Flocking Simulation
==============================================
Classic multi-agent emergent-behavior algorithm (Reynolds, 1987): each
agent follows three simple local rules — separation, alignment, and
cohesion — and complex flocking behavior emerges with no central
coordinator. The same principle underlies real swarm-robotics systems.

Usage
-----
    python boids_flocking.py
"""

import matplotlib.pyplot as plt
import numpy as np


N_BOIDS = 60
WORLD_SIZE = 100
PERCEPTION_RADIUS = 15.0
MAX_SPEED = 2.0
N_STEPS = 400

W_SEPARATION = 1.0
W_ALIGNMENT = 2.5
W_COHESION = 1.0


def limit_magnitude(vec, max_mag):
    mag = np.linalg.norm(vec)
    if mag > max_mag:
        return vec / mag * max_mag
    return vec


def step(positions, velocities):
    n = len(positions)
    new_velocities = velocities.copy()

    for i in range(n):
        diffs = positions - positions[i]
        dists = np.linalg.norm(diffs, axis=1)
        dists[i] = np.inf
        neighbors = dists < PERCEPTION_RADIUS

        if not np.any(neighbors):
            continue

        # separation: steer away from nearby boids, weighted by inverse distance
        close = dists < PERCEPTION_RADIUS / 2
        if np.any(close):
            separation = -np.sum(diffs[close] / (dists[close, None] ** 2), axis=0)
        else:
            separation = np.zeros(2)

        # alignment: match average heading of neighbors
        alignment = velocities[neighbors].mean(axis=0) - velocities[i]

        # cohesion: steer toward the centroid of neighbors
        centroid = positions[neighbors].mean(axis=0)
        cohesion = centroid - positions[i]

        accel = (W_SEPARATION * separation + W_ALIGNMENT * alignment + W_COHESION * cohesion) * 0.1
        new_velocities[i] = limit_magnitude(velocities[i] + accel, MAX_SPEED)

    new_positions = positions + new_velocities

    # bounce off the world boundary (avoids toroidal wraparound distance issues,
    # which would otherwise distort separation/cohesion near the edges)
    for dim in (0, 1):
        below = new_positions[:, dim] < 0
        above = new_positions[:, dim] > WORLD_SIZE
        new_velocities[below | above, dim] *= -1
        new_positions[:, dim] = np.clip(new_positions[:, dim], 0, WORLD_SIZE)

    return new_positions, new_velocities


def demo():
    rng = np.random.default_rng(6)
    positions = rng.uniform(0, WORLD_SIZE, size=(N_BOIDS, 2))
    velocities = rng.uniform(-1, 1, size=(N_BOIDS, 2))

    snapshots = []
    for i in range(N_STEPS):
        positions, velocities = step(positions, velocities)
        if i in (0, N_STEPS // 3, 2 * N_STEPS // 3, N_STEPS - 1):
            snapshots.append((positions.copy(), velocities.copy()))

    # rough "flocking" metric: average pairwise heading alignment at the end
    final_vel = snapshots[-1][1]
    normed = final_vel / (np.linalg.norm(final_vel, axis=1, keepdims=True) + 1e-9)
    alignment_score = np.linalg.norm(normed.mean(axis=0))  # 1.0 = perfectly aligned flock
    print(f"Final flock alignment score: {alignment_score:.3f} (0 = random, 1 = perfectly aligned)")

    fig, axes = plt.subplots(1, 4, figsize=(18, 5))
    titles = ["step 0 (random init)", f"step {N_STEPS // 3}", f"step {2 * N_STEPS // 3}", f"step {N_STEPS - 1} (final)"]
    for ax, (pos, vel), title in zip(axes, snapshots, titles):
        headings = np.arctan2(vel[:, 1], vel[:, 0])
        ax.quiver(pos[:, 0], pos[:, 1], np.cos(headings), np.sin(headings),
                   angles="xy", scale=25, width=0.006, color="steelblue")
        ax.set_xlim(0, WORLD_SIZE)
        ax.set_ylim(0, WORLD_SIZE)
        ax.set_title(title, fontsize=10)
        ax.set_aspect("equal")

    plt.suptitle(f"Boids Flocking — {N_BOIDS} Agents (final alignment: {alignment_score:.2f})", fontsize=13)
    plt.tight_layout()
    plt.savefig("boids_flocking.png", dpi=120)
    print("Saved visualization to boids_flocking.png")
    plt.show()


if __name__ == "__main__":
    demo()
