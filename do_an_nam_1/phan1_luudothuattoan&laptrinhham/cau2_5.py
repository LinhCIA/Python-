# 5. Viết chương trình chính
# a. Sinh ngẫu nhiên list các số thực;
# b. Lưu list vào tập tin văn bản;
# c. Sắp xếp list theo chiều giảm dần;
# d. Lưu list ở câu (c) vào tập tin văn bản;
# e. Tìm kiếm số n trong list ở câu (d);
from cau2_1 import sinh_ngau_nhien
from cau2_2 import sap_xep
from cau2_3 import tim_kiem_2
from cau2_4 import luu_list 

def main():
    # Ý a
    a = abs(int(input("Nhập số phần tử mà bạn muốn có trong list : ")))
    list1 = sinh_ngau_nhien(a)
    print("List được sinh ngẫu nhiên là\n",list1)
    #Ý b
    c1 = list1
    print("Bạn muốn lưu list  ở dạng tập tin văn bản. Vui lòng nhấn phím 1")
    print("hoặc")
    print("Bạn muốn lưu list ở trên dạng nhị phân. Vui lòng nhấn phím 2")
    nhan = int(input(""))
    print("nhan = ", nhan)
    luu_list(nhan, c1)
    # Ý c
    list2 = sap_xep(list1, False)
    print("List sau khi được sắp xếp theo thứ tự dảm dần là:\n ", list2)
    #Ý d
    c2 = list2
    print("Bạn muốn lưu list trên ở dạng tập tin văn bản. Vui lòng nhấn phím 1")
    print("hoặc")
    print("Bạn muốn lưu list trên ở dạng nhị phân. Vui lòng nhấn phím 2")
    nhan = int(input(""))
    print("nhan = ", nhan)
    luu_list(nhan, c2)
    # Ý e
    n = float(input("Nhập số mà bạn muốn tìm : "))
    tim_kiem_2(c2, n)

if __name__ == "__main__":
    main()