import numpy as np

def compute_plane_equation(A, B, C):
    AB = np.subtract(B, A)
    AC = np.subtract(C, A)
    n = np.cross(AB, AC)

    x0, y0, z0 = A
    d = np.dot(n, A)
    plane_eq = f"{n[0]:.2f}x + {n[1]:.2f}y + {n[2]:.2f}z = {d:.2f}"

    return plane_eq, n