#Ý 1 :
import numpy as np
np.random.seed(123)

def matrix_x(a1:int, b1:int, n1:int):
    x = np.random.uniform(low=a1, high=b1, size=(1*n1)).reshape((1,n1))
    return x

def matrix_A(a2:int, b2:int, m2:int, n2:int):
    A = np.random.uniform(low=a2, high=b2, size=(m2*n2)).reshape((m2,n2))
    return A

def matrix_B(a3:int, b3:int, m3:int, n3:int):
    B = np.random.uniform(low=a3, high=b3, size=(m3*n3)).reshape((m3,n3))
    return B

import math

def ham1(a1:int, b1:int, n1:int, a2:int, b2:int, m2:int, n2:int):
    x = matrix_x(a1, b1, n1)
    A = matrix_A(a2, b2, m2, n2)
    if math.isclose(n1,m2):
        f1 = np.dot(x,A)
        print("Kết quả phép nhân x.A:")
        for hang1 in f1:
            for element1 in hang1:
                print("{:>25}".format(element1), end="")
            print()
    else:
        print("Kích thước của 2 ma trận không tương thích\n","Không tính được\n","Vui lòng kiểm tra lại!")
#Ý 2 :
def ham2(a2:int, b2:int, m2:int, n2:int, a3:int, b3:int, m3:int, n3:int):
    A = matrix_A(a2, b2, m2, n2)
    B = matrix_B(a3, b3, m3, n3)
    if (m2==m3) and (n2==n3):
        f2 = np.multiply(A,B)
        print("Kết quả của phép nhân Hadamard A°B:")
        for hang2 in f2:
            for element2 in hang2:
                print("{:>25}".format(element2), end="")
            print()

def ham3(a2:int, b2:int, m2:int, n2:int, a3:int, b3:int, m3:int, n3:int):
    A = matrix_A(a2, b2, m2, n2)
    B = matrix_B(a3, b3, m3, n3)
    f3 = np.dot((A.transpose()),B)
    print("Kết quả của phép toán AT.B:")
    for hang3 in f3:
        for element3 in hang3:
            print("{:>25}".format(element3), end="")
        print()

#Ý 3 :
def main():
    # Nhập dữ liệu
    a1 = int(input("Các phần tử của vector x được sinh ngẫu nhiên bắt đầu từ giá trị = " ))
    b1 = int(input("Các phẩn tử của vector x được sinh ngẫu nhiên kết thúc tại giá trị = "))
    n1 = int(input("Nhập số phần tử mà bạn muốn có ở vector x = "))
    a2 = int(input("Các phần tử của ma trận A được sinh ngẫu nhiên bắt đầu từ giá trị = "))
    b2 = int(input("Các phần tử của ma trận A được sinh ngẫu nhiên kết thúc tại giá trị = "))
    m2 = int(input("Nhập số hàng mà bạn muốn ở ma trận A = "))
    n2 = int(input("Nhập số cột  mà bạn muốn ở ma trận A = "))
    a3 = int(input("Các phần tử của ma trận B được sinh ngẫu nhiên bắt đầu từ giá trị = "))
    b3 = int(input("Các phần tử của ma trận B được sinh ngẫu nhiên kết thúc tại giá trị = "))
    m3 = int(input("Nhập số hàng mà bạn muốn ở ma trận B = "))
    n3 = int(input("Nhập số cột  mà bạn muốn ở ma trận B = "))
    # Gọi hàm
    ham1(a1, b1, n1, a2, b2, m2, n2)
    ham2(a2, b2, m2, n2, a3, b3, m3, n3)
    ham3(a2, b2, m2, n2, a3, b3, m3, n3)

# Chạy hàm chính
if __name__=="__main__":
    main()