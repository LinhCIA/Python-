#Doc tap tin o bai 3 va in ket qua ra man hinh
def exercises4():
    ten_tap_tin = input("Nhap tap tin o exercises3:")
    with open(ten_tap_tin, 'r', encoding='utf-8') as f:
        print(f.read())
def main():
    exercises4()
if __name__=="__main__":
    main() 

