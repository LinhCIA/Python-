#Ý 1: Viết hàm giải hệ phương trình
from sympy import *

def giai_he_phuong_trinh():
    x, y, z = symbols("x y z")
    eq1 = Eq(2*x - 5*y + z, -5)
    eq2 = Eq(4*x + 2*y - 2*z, 2)
    eq3 = Eq(x + y - z, 0)
    f1 = solve((eq1, eq2, eq3), (x, y, z))
    print("Nghiệm của hệ phương trình là: ",f1)

#Ý 2 : Viết hàm tình giới hạn
def tinh_gioi_han():
    x = symbols("x")
    eq4 = (x**3 - 3*x**2)**1/3 + (x**2-2*x)**1/2
    f2 = limit(eq4, x, oo)
    print("Kết quả giới hạn =",f2)

#Ý 3 : Viết hàm tính đạo hàm
def tinh_dao_ham():
    x = symbols("x")
    eq5 = (2*x-1)/(x+2)
    f3 = diff(eq5, x)
    print("Kết quả đạo hàm =",f3)

#Ý 4: Viết hàm tính nguyên hàm
def tinh_nguyen_ham():
    x = symbols("x")
    eq6 = x/(x**2+1)
    f4 = integrate(eq6,x)
    print("Họ nguyên hàm =",f4,"+ C")

# Ý 5: Viết hàm tính tích phân
def tinh_tich_phan():
    x = symbols("x")
    eq7 = (1-x*tan(x))/((x**2)*cos(x)+x)
    f5 = integrate(eq7, (x, (2*pi)/3, pi))
    print("Kết quả tích phân =",f5)
# Ý 6: Viết chương trình chính
def main():
    giai_he_phuong_trinh()
    tinh_gioi_han()
    tinh_dao_ham()
    tinh_nguyen_ham()
    tinh_tich_phan()

if __name__=="__main__":
    main()