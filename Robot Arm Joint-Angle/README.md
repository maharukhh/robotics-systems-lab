# Robot Arm Joint-Angle Form

An interactive 3-DOF planar robot arm (base rotation, shoulder, elbow)
rendered as SVG. Slider controls for each joint angle and link length
drive a live forward-kinematics calculation, updating the arm's pose and
end-effector position in real time.

## Run it
Open `index.html` in a browser — no build step or dependencies required.

## Concepts demonstrated
- **Forward kinematics** — computing end-effector position from a chain
  of joint angles and link lengths using trigonometric transforms
- **Coordinate transforms** — each joint's position depends on the
  cumulative rotation and offset of the joints before it
- **Reactive rendering** — range inputs drive SVG redraws on every
  change, keeping the visual pose in sync with the underlying math
- **Reading derived state** — displaying computed end-effector (x, y)
  coordinates rather than raw input values

## Next steps
- Add inverse kinematics: let the user drag the end-effector directly and
  solve backward for the joint angles that reach it
- Extend to a 3D arm with three.js, or add joint limits and collision
  boundaries for a more realistic simulation
