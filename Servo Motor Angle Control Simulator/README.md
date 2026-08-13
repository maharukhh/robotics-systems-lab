# Servo Motor Angle Control Simulator

Drag a 0°–180° slider to rotate a simulated servo arm (SVG) and see the
matching PWM control-pulse waveform update in real time — using standard
hobby-servo timing (a 1ms–2ms pulse width within a 20ms / 50Hz period).

## Run it
Open `index.html` in a browser.

## Concepts demonstrated
- **SVG transforms** — rotating the servo arm live via `transform:
  rotate()`, driven directly by slider input
- **Angle-to-PWM mapping** — converting a 0°–180° angle into the actual
  pulse width a real servo expects, the core signal-encoding step
  between software and hardware
- **Waveform rendering** — drawing the resulting PWM signal on canvas so
  the pulse width and period are visible, not just implied by the angle
- **Real-time synchronization** — keeping the visual arm pose and the
  waveform display consistent as input changes

## Next steps
- Add servo speed/acceleration limiting so the arm eases toward the
  target angle instead of snapping instantly
- Support multiple servos side by side to simulate a multi-joint gripper
  or pan-tilt mount
