import matplotlib.pyplot as plt
from Câu3_1 import ham_y1
from Câu3_1 import ham_x

# Xây dựng hàm y'
def ham_y2(x):
    y2 = 4*x**3 - 4*x
    return y2

#Vẽ đồ thị hàm y'
def main():
    x = ham_x()
    y2 = ham_y2(x)
    fig, ax = plt.subplots()
    ax.plot(x, y2, "red", label=r"$y'=4x^{3}-4x$")
    ax.set_xlabel("Trục hoành - x")
    ax.set_ylabel("Trục tung - y")
    ax.set_title("Đồ thị 2")
    ax.legend()
    plt.show()

if __name__=="__main__":
    main()







