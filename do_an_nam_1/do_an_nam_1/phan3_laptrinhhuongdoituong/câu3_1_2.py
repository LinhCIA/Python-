from câu3_1_1 import NhanVien

# Hàm nhập dữ liệu cho 1 list các đối tượng thuộc lớp NhanVien;
def nhap_nhan_vien():
    list1 = []
    print("DANH SÁCH NHÂN VIÊN")
    n = abs(int(input("Số nhân viên cần điền thông tin: ")))
    for i in range(n):
        print("STT :", i+1)
        name = input("Họ và tên: ")
        age = input("Độ tuổi: ")
        salary = input("Mức lươnng: ")
        nv = NhanVien(name,age, salary)
        list1.append(nv)
    return list1

# Hàm hiển thị list các đối tượng thuộc lớp NhanVien ra màn hình;
def hien_thi():
    print("DANH SÁCH NHÂN VIÊN")
    list2 = nhap_nhan_vien()
    for i in list2:
        print(i)

# Hàm sắp xếp list các đối tượng thuộc lớp NhanVien theo chiều giảm dần của độ tuổi;
def sap_xep(a):
    a = sorted(a, key=lambda x: x[1], reverse=True)
    print(a)
    return a

# Hàm lưu list các đối tượng thuộc lớp NhanVien vào tập tin nhị phân;
import os
import pickle

def luu_nhan_vien(ten_tap_tin: str, objs: list[NhanVien]):
    try:
        with open(os.path.join(ten_tap_tin), 'wb') as f:
            pickle.dump(objs, f)
        print('Hoan thanh qua trinh ghi du lieu vao tap tin')
    except Exception as e:
        print(e)
        print('Xay ra loi trong qua trinh ghi file')
# Hàm đọc list các đối tượng thuộc lớp NhanVien từ tập tin nhị phân;

def doc_nhan_vien(ten_tap_tin: str) -> list[NhanVien]:
    try:
        with open(os.path.join(ten_tap_tin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        return None

def in_list_nhan_vien(content: list[NhanVien]):
    for item in content:
        print(item)












