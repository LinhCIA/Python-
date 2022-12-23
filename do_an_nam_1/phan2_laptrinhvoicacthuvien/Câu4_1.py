# Vẽ đồ thị mặt yên ngựa

import numpy as np
import matplotlib.pyplot as plt

# Sinh dữ liệu
def ham_x():
    x = np.linspace(start=-10.0, stop=10.0, num=2000)
    return x

def ham_y():
    y = np.linspace(start=-10.0, stop=10.0, num=2000)
    return y

# Xây dựng hàm
def ham_z(x,y):
    z = (x/3)**2 - (y/2)**2
    return z

# Vẽ
def ve_1():
    x = ham_x()
    y = ham_y()
    x, y = np.meshgrid(x, y)
    z = ham_z(x, y)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surf = ax.plot_surface(x, y, z, cmap="Set1", linewidth=0, antialiased=False)
    ax.set_xlabel("Trục x")
    ax.set_ylabel("Trục y")
    ax.set_zlabel("Trục z")
    ax.set_title("Mặt yên ngựa")
    ax.set_zlim(-30,20)
    fig.colorbar(surf, shrink=1, aspect=5)
    plt.show()

