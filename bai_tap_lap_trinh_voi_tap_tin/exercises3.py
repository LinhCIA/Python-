def exercises3():
    #Nhap tap tin tu ban phim
    ten_tap_tin = input("Ten tap tin la:")
    #Nhap mot chuoi ki tu tu ban phim
    n = input("Nhap chuoi ki tu tuy y:")
    #Ghi chuoi ki tu nay vao cuoi tap tin o tren
    with open(ten_tap_tin, "a", encoding='utf-8') as f:
        f.write(n)
def main():
    exercises3()
if __name__=="__main__":
    main()