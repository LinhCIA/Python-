# 3.Tìm kiếm số n trong list:
# a. Nếu không tìm thấy thì thông báo ra màn hình là không tìm thấy số n trong list;
# b. Nếu tìm thấy thì hiển thị ra màn hình tất cả các vị trí trong list có giá trị bằng với n
import math

def tim_kiem(y:list, n:int):
    vitri = []
    if n in y:
        for i in range(len(y)):
            if math.isclose(y[i], n):
                vitri.append(i)
        return vitri
    else:
        return None

def tim_kiem_2(y, n):
    z = tim_kiem(y, n)
    if z == None:
        print("Không tìm thấy")
    else:
        print("Tất cả vị trí trong list có giá trị bằng", n, "là vị trí thứ", z)