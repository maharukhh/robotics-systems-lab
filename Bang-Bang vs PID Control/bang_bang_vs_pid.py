"""
Bang-Bang vs PID Control Comparison
==============================================
Contrasts the simplest possible feedback controller (bang-bang / on-off
control, e.g. a household thermostat) against PID control on the same
first-order plant, showing the classic trade-off: bang-bang is trivial to
implement but oscillates around the setpoint, while PID converges
smoothly with far less steady-state chatter.

"""

import matplotlib.pyplot as plt
import numpy as np


def plant_step(x, u, dt, tau=1.0):
    """First-order plant: dx/dt = (u - x) / tau  (e.g. a heating/cooling system)."""
    dx = (u - x) / tau
    return x + dx * dt


def simulate_bang_bang(setpoint, x0=0.0, dt=0.05, steps=800, on_power=35.0, hysteresis=0.5):
    x = x0
    u = on_power  # start heating
    history = [x]
    for _ in range(steps):
        if x < setpoint - hysteresis:
            u = on_power
        elif x > setpoint + hysteresis:
            u = 0.0
        # else: keep previous u (this is the hysteresis "dead band" a real thermostat uses)
        x = plant_step(x, u, dt)
        history.append(x)
    return np.array(history)


class PID:
    def __init__(self, kp, ki, kd, dt):
        self.kp, self.ki, self.kd, self.dt = kp, ki, kd, dt
        self.integral = 0.0
        self.prev_error = 0.0

    def compute(self, error):
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error
        return self.kp * error + self.ki * self.integral + self.kd * derivative


def simulate_pid(setpoint, x0=0.0, dt=0.05, steps=800, kp=2.5, ki=0.6, kd=0.4):
    pid = PID(kp, ki, kd, dt)
    x = x0
    history = [x]
    for _ in range(steps):
        error = setpoint - x
        u = pid.compute(error)
        x = plant_step(x, u, dt)
        history.append(x)
    return np.array(history)


def demo():
    setpoint = 20.0
    bb_history = simulate_bang_bang(setpoint)
    pid_history = simulate_pid(setpoint)
    t = np.arange(len(bb_history)) * 0.05

    bb_settled = bb_history[3 * len(bb_history) // 4:]
    pid_settled = pid_history[3 * len(pid_history) // 4:]
    print(f"Steady-state oscillation (2nd half of run) — Bang-Bang std: {np.std(bb_settled):.3f}, PID std: {np.std(pid_settled):.4f}")

    fig, ax = plt.subplots(figsize=(10, 5.5))
    ax.axhline(setpoint, color="gray", linestyle="--", linewidth=1, label="setpoint")
    ax.plot(t, bb_history, color="darkorange", linewidth=1.5, label="bang-bang control")
    ax.plot(t, pid_history, color="steelblue", linewidth=2, label="PID control")
    ax.set_title("Bang-Bang vs PID Control on the Same Plant")
    ax.set_xlabel("time (s)")
    ax.set_ylabel("system output")
    ax.legend()
    plt.savefig("bang_bang_vs_pid.png", dpi=120)
    print("Saved visualization to bang_bang_vs_pid.png")
    plt.show()


if __name__ == "__main__":
    demo()
