import matplotlib.pyplot as plt
from Câu3_1 import ham_x

# Xây dựng hàm y''
def ham_y3(x):
    y3 = 12*x**2 - 4
    return y3

# Vẽ đồ thị hàm y''
def main():
    x = ham_x()
    y3 = ham_y3(x)
    fig, ax = plt.subplots()
    ax.plot(x, y3, "red", label=r"$y''=12x^{2}-4$")
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.set_title("Đồ thị 3")
    ax.legend()
    plt.show()

if __name__=="__main__":
    main()
