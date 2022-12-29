# Vẽ đồ thị hàm y, y', y'', y'''
import matplotlib.pyplot as plt
import numpy as np

def ham_x():
    x = np.linspace(-10, 10, 30)
    return x

def ham_bac_4(x):
    b4 = x**4-2*x**2-3
    return b4
def ham_bac_3(x):
    b3 = 4*x**3 - 4*x
    return b3
def ham_bac_2(x):
    b2 = 12*x**2 - 4
    return b2
def ham_bac_1(x):
    b1 = 24*x
    return b1
def ve():
    fig, (ax) = plt.subplots()
    x = ham_x()
    y4 = ham_bac_4(x)
    ax.plot(x, y4, '*-', label=r"$y= x^{4} - 2x^{2} -3$")
    y3 = ham_bac_3(x)
    ax.plot(x, y3, 'D-', label=r"$y'=4x^{3}-4x$")
    y2 = ham_bac_2(x)
    ax.plot(x, y2, 'ro-', label=r"$y''=12x^{2}-4$")
    y1 = ham_bac_1(x)
    ax.plot(x, y1, 'g^-', label=r"$y'''=24x$")
    ax.set_title("Đồ thị hàm y, y', y'', y'''")
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.legend()
    plt.show()
ve()