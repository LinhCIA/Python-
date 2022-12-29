# Vẽ đồ thị mặt hyperbolic 1 tầng

import numpy as np
import matplotlib.pyplot as plt

# Sinh dữ liệu
def ham_x():
    x = np.linspace(start=-10.5, stop=10.0, num=1000)
    return x

def ham_y():
    y = np.linspace(start=-10.0, stop=10.0, num=1000)
    return y

# Xậy dựng hàm
def ham_z1(x,y):
    z1 = 2 * (((x**2/9) + (y**2/25) - 1)**(1/2))
    return z1

def ham_z2(x,y):
    z2 = (-2) * (((x**2/9) + (y**2/25) - 1)**(1/2))
    return z2

# Vẽ
def ve_2():
    x = ham_x()
    y = ham_y()
    x, y = np.meshgrid(x, y)
    z1 = ham_z1(x, y)
    z2 = ham_z2(x, y)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    hyperbolic_surf = ax.plot_surface(x, y, z1, cmap="Blues_r", linewidth=0, antialiased=False)
    hyperbolic_surf = ax.plot_surface(x, y, z2, cmap="Blues_r", linewidth=0, antialiased=False)
    ax.set_xlabel("Trục x")
    ax.set_ylabel("Trục y")
    ax.set_zlabel("Trục z")
    ax.set_title("Hyperbolic 1 tầng")
    ax.set_zlim(-8, 8)
    fig.colorbar(hyperbolic_surf, shrink=1, aspect=5)
    plt.show()
ve_2()