import numpy as np
import matplotlib.pyplot as plt
# Sinh dữ liệu
def ham_x():
    x = np.linspace(start=-10.0, stop=10.0, num=20000)
    return x

# Xây dựng hàm số y
def ham_y1(x):
    y1 = x**4 - 2*x**2 - 3
    return y1

# Vẽ đồ thị hàm y
def main():
    x = ham_x()
    y1 = ham_y1(x)
    fig, ax = plt.subplots()
    ax.plot(x, y1, "red", label=r"$y= x^{4} - 2x^{2} -3$")
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.set_title("Đồ thị 1")
    ax.legend()
    plt.show()

if __name__=="__main__":
    main()






