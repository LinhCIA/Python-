# Vẽ đồ thị mặt cầu

import numpy as np
import matplotlib.pyplot as plt

# Sinh dữ liệu
def ham_x():
    x = np.linspace(start=-5.0, stop=5.0, num=3000)
    return x

def ham_y():
    y = np.linspace(start=-5.5, stop=5.5, num=3000)
    return y

# Dựng hàm
def ham_z1(x,y):
    z1 = 4 + ((4-(x**2 + 2*x + 4) - (y**2 - 2*y+1))**(1/2))
    return z1

def ham_z2(x,y):
    z2 = 4 - ((4-(x**2 + 2*x + 4) - (y**2 - 2*y+1))**(1/2))
    return z2

# Vẽ
def ve_3():
    x = ham_x()
    y = ham_y()
    x, y = np.meshgrid(x, y)
    z1 = ham_z1(x, y)
    z2 = ham_z2(x, y)
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    mat_cau_surf = ax.plot_surface(x, y, z1, cmap="Accent_r", linewidth=0, antialiased=False)
    mat_cau_surf = ax.plot_surface(x, y, z2, cmap="Accent_r", linewidth=0, antialiased=False)
    ax.set_xlabel("Trục x")
    ax.set_ylabel("Trục y")
    ax.set_zlabel("Trục z")
    ax.set_title("Mặt cầu")
    ax.set_zlim(0,7)
    fig.colorbar(mat_cau_surf, shrink=1, aspect=5)
    plt.show()
ve_3()



