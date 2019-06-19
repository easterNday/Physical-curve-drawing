import numpy as np
import matplotlib.pyplot as plt

def projectile(V_initial, theta, bouyancy=True, drag=True):
    g = 9.81
    m = 1
    C = 0.47
    r = 0.5
    S = np.pi*pow(r, 2)
    ro_mars = 0.0175

    time = np.linspace(0, 100, 10000)
    tof = 0.0
    dt = time[1] - time[0]
    bouy = ro_mars*g*(4/3*np.pi*pow(r, 3))
    gravity = -g * m
    V_ix = V_initial * np.cos(theta)
    V_iy = V_initial * np.sin(theta)
    v_x = V_ix
    v_y = V_iy
    r_x = 0.0
    r_y = 0.0
    r_xs = list()
    r_ys = list()
    r_xs.append(r_x)
    r_ys.append(r_y)
    # This gets a bit 'hand-wavy' but as dt -> 0 it approaches the analytical solution.
    # Just make sure you use sufficiently small dt (dt is change in time between steps)
    for t in time:
        F_x = 0.0
        F_y = 0.0
        if (bouyancy == True):
            F_y = F_y + bouy
        if (drag == True):
            F_y = F_y - 0.5*C*S*ro_mars*pow(v_y, 2)
            F_x = F_x - 0.5*C*S*ro_mars*pow(v_x, 2) * np.sign(v_y)
        F_y = F_y + gravity

        r_x = r_x + v_x * dt + (F_x / (2 * m)) * dt**2
        r_y = r_y + v_y * dt + (F_y / (2 * m)) * dt**2
        v_x = v_x + (F_x / m) * dt
        v_y = v_y + (F_y / m) * dt
        if (r_y >= 0.0):
            r_xs.append(r_x)
            r_ys.append(r_y)
        else:
            tof = t
            r_xs.append(r_x)
            r_ys.append(r_y)
            break

    return r_xs, r_ys, tof

v = 30
theta = np.pi/4

fig = plt.figure(figsize=(8,4), dpi=100)
r_xs, r_ys, tof = projectile(v, theta, True, True)
plt.plot(r_xs, r_ys, 'g:', label="Gravity, Buoyancy, and Drag")
r_xs, r_ys, tof = projectile(v, theta, False, True)
plt.plot(r_xs, r_ys, 'b:', label="Gravity and Drag")
r_xs, r_ys, tof = projectile(v, theta, False, False)
plt.plot(r_xs, r_ys, 'k:', label="Gravity")
plt.title("Trajectory", fontsize=14)
plt.xlabel("Displacement in x-direction (m)")
plt.ylabel("Displacement in y-direction (m)")
plt.ylim(bottom=0.0)
plt.legend()
plt.show()