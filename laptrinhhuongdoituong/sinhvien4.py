from sinhvien1 import SinhVien
import os
import pickle

def ghi_sinh_vien(ten_taptin: str, objs: list[SinhVien]):
    try:
        with open(os.path.join(ten_taptin), 'wb') as f:
            pickle.dump(objs, f)
        print("Lưu thành công!")
    except Exception as e:
        print("Xảy ra lỗi trong file!")
        print(e)

def doc_sinh_vien(ten_taptin: str) -> list[SinhVien]:
    try:
        with open(os.path.join(ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        print(e)
        return None

def in_list_sinh_vien(content: list[SinhVien]):
    for i in content:
        print(i)

def main():
    ten_tap_tin = input("Nhập tập tin cần ghi và đọc (Bao gồm cả nguồn): ")
    sv1 = [SinhVien('Thanh Linh ', 2004, 10.0),
           SinhVien('Duy', 2005, 12.0),
           SinhVien('Tri', 2005, 3.0)]
    ghi_sinh_vien(ten_tap_tin, sv1)
    doc = doc_sinh_vien(ten_tap_tin)
    in_list_sinh_vien(doc)
    print('ket thuc chuong trinh')

if __name__ == '__main__':
    main()