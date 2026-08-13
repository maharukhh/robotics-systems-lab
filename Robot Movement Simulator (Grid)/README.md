# Robot Movement Simulator (Grid)

A simulated robot — rendered as a dot on a 12×12 grid — moves in
response to arrow keys or on-screen buttons, staying within grid bounds
and tracking a live step count.

## Run it
Open `index.html` in a browser, click the grid to focus it, then use the
arrow keys (or the on-screen buttons) to move.

## Concepts demonstrated
- **Keyboard event handling** — capturing and mapping `keydown` events
  (arrow keys) to discrete movement commands
- **Grid rendering** — building a uniform 2D grid layout with CSS Grid
- **Bounds-checked coordinate movement** — clamping (x, y) position
  updates to valid grid limits, a foundational pattern for path planning
  and navigation logic
- **State tracking** — maintaining and displaying step count as
  movement state changes

## Next steps
- Add static obstacles the robot must navigate around
- Add a trail overlay showing previously visited cells
- Extend with a simple pathfinding target (move the robot to a goal cell
  automatically)
