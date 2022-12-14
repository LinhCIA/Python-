from sinhvien1 import SinhVien
def main():
    sv = [SinhVien("Le Thanh Linh",2004,10),
          SinhVien("Le Duy Anh",2004,9),
          SinhVien("Le Khanh Duy", 2004, 8),
          ]
    for i in sv:
        print(i)
if __name__=="__main__":
    main()
