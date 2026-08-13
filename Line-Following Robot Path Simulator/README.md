# Line-Following Robot Path Simulator

A simulated robot follows a predefined wavy track using proportional
correction against simulated sensor noise and drift — a simplified model
of how real IR-sensor line followers stay centered on a line.

## Run it
Open `index.html` in a browser and click **Start**.

## Concepts demonstrated
- **Parametric curve tracks** — defining the path as a `trackPoint(t)`
  function and computing tangent direction via finite differences
- **Proportional (P) control** — continuously correcting the robot's
  lateral offset back toward the line, the core feedback loop behind
  real line-following hardware
- **Animation loop** — driving continuous motion and correction with
  `requestAnimationFrame` for smooth, frame-rate-independent updates
- **Simulated sensor noise** — modeling drift/uncertainty the way real
  IR sensors would introduce it, rather than assuming perfect tracking

## Next steps
- Replace the offset-noise mock with real dual-sensor black/white
  detection sampled from canvas pixels beneath the robot
- Add sharper turns or track branches to test correction limits
- Introduce PID (not just P) control for smoother recovery from
  larger offsets
