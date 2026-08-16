# Boids Flocking Simulation

A Python-based multi-agent swarm simulation inspired by Craig Reynolds' classic Boids algorithm. It demonstrates how simple local rules can produce coordinated flocking behavior without a central controller.

## Run it

Prints a final "flock alignment score" (0 = random headings, 1 = perfectly aligned), and saves `boids_flocking.png`: four snapshots showing agents evolve from random initial headings into coherent moving flocks.

## The three rules

1. **Separation** — steer away from agents that are too close, to avoid collisions.
2. **Alignment** — steer to match the average heading of nearby agents.
3. **Cohesion** — steer toward the average position (centroid) of nearby agents.

No central coordinator controls the flock. Complex group behavior emerges from simple local interactions, making this a practical example of swarm robotics and multi-agent systems.

## Dependencies

`numpy`, `matplotlib`

## Key Concepts

Swarm Robotics • Multi-Agent Systems • Emergent Behavior • Decentralized Control • Flocking Algorithms • Agent-Based Simulation
