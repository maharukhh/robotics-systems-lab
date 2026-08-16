# Boids Flocking Simulation

Classic multi-agent emergent-behavior algorithm (Craig Reynolds, 1987): each agent follows three simple local rules, and complex, realistic flocking behavior emerges with no central coordinator — a core principle behind real swarm-robotics systems.

## Run it

Prints a final "flock alignment score" (0 = random headings, 1 = perfectly aligned), and saves `boids_flocking.png`: four snapshots showing agents evolve from random initial headings into coherent moving flocks.

## The three rules

1. **Separation** — steer away from agents that are too close, to avoid collisions.
2. **Alignment** — steer to match the average heading of nearby agents.
3. **Cohesion** — steer toward the average position (centroid) of nearby agents.

No agent has any global knowledge of the flock — each only reacts to neighbors within its local perception radius. The flocking behavior that emerges is a good illustration of why swarm robotics can achieve complex group behavior from simple, fully decentralized individual rules.

## Dependencies

`numpy`, `matplotlib`
