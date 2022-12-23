import matplotlib.pyplot as plt
from Câu3_1 import ham_x

# Xây dựng hàm y'''
def ham_y4(x):
    y4 = 24*x
    return y4

# Vẽ đồ thị hàm y'''
def main():
    x = ham_x()
    y4 = ham_y4(x)
    fig, ax = plt.subplots()
    ax.plot(x, y4, "red", label=r"$y'''=24x$")
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.set_title("Đồ thị 4")
    ax.legend()
    plt.show()

if __name__=="__main__":
    main()