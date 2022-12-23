# 4. Viết hàm lưu list vào tập tin có tùy chọn tham số để xác định là lưu tập tin văn bản hay tập tin nhị phân;
import os
import pickle

def luu_list(nhan:int, c:list):
    ten_tap_tin = input("Nhập tên tập tin mà bạn muốn lưu ( Bao gồm cả đường dẫn ): ")
    if nhan == 1:
        with open(ten_tap_tin, "w") as f:
            f.write(f"{c}")
            f.close()
        print("Lưu thành công!")
    elif nhan == 2:
        try:
            with open(os.path.join(ten_tap_tin), 'wb') as f:
                pickle.dump(c, f)
            print("Lưu thành công!")
        except Exception as e:
            print("Xảy ra lỗi trong file!")
            print(e)
    else:
        print("Vui lòng nhập lại!")
