# Motor Speed Control UI (PWM Duty-Cycle Slider)

Drag a duty-cycle slider (0–100%) to spin a simulated motor/fan faster or
slower, with an estimated RPM readout and a live PWM waveform showing the
on/off pulse pattern that would actually drive a real DC motor.

## Run it
Open `index.html` in a browser.

## Concepts demonstrated
- **PWM (Pulse Width Modulation)** — the standard technique for
  controlling DC motor speed digitally by varying the fraction of time
  the signal is "on" within each cycle
- **Duty cycle to speed mapping** — translating a 0–100% duty cycle into
  visual rotation speed via `requestAnimationFrame`
- **Waveform rendering** — drawing the repeating PWM pulse train on
  canvas so the relationship between duty cycle and signal shape is
  visible, not just implied
- **Real-time feedback** — keeping the RPM readout, motor animation, and
  waveform display all synchronized as the slider changes

## Next steps
- Add a direction toggle (forward/reverse) to simulate H-bridge control
- Simulate motor acceleration/deceleration (ramping) instead of instant
  speed changes, closer to real motor inertia
