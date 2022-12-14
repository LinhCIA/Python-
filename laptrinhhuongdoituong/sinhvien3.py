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

def doc_sinh_vien(ten_taptin: str) -> SinhVien:
    try:
        with open(os.path.join(ten_taptin), 'rb') as f:
            sv = pickle.load(f)
        return sv
    except Exception as e:
        print(e)
        return None

def main():
    ten_tap_tin = input("Nhập tập tin cần ghi hoặc cần đọc (Bao gồm cả đường dẫn): ")
    sv1 = [SinhVien('Khanh Van', 2004, 10.0)]
    ghi_sinh_vien(ten_tap_tin, sv1)
    doc = doc_sinh_vien(ten_tap_tin)
    print(doc)
    print('ket thuc chuong trinh')

if __name__ == '__main__':
    main()



