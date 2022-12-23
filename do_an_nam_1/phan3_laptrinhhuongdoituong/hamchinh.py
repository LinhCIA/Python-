# Gọi các hàm ở các câu trên
from câu3_1_2 import nhap_nhan_vien, hien_thi, sap_xep, luu_nhan_vien, doc_nhan_vien

# Hàm chính
def main():
    # Ý 2
    nhap_nhan_vien()
    # Ý 3
    hien_thi()
    # Ý 4
    list3 = nhap_nhan_vien()
    sx = sap_xep(list3)
    print("Danh sách nhân viên(theo chiều giảm dần của độ tuổi): \n", sx)
    # Ý 5
    ten_tap_tin1 = input("Nhập tên tập tin mà bạn muốn lưu(Bao gồm đường dẫn): ")
    luu_nhan_vien(ten_tap_tin1, sx)
    # Ý 6
    ten_tap_tin2 = input("Nhập tên tập tin mà bạn muốn đọc(Bao gồm đường dẫn): ")
    doc_nhan_vien(ten_tap_tin2)
    print("OKELA")
if __name__=="__main__":
    main()
