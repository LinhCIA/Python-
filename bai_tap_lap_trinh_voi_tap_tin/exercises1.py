def exercises1():
    #nhap mot chuoi ki tu
    n = input("Nhap mot chuoi tuy y :")
    #nhap ten tap tin tu ban phim
    ten_tap_tin = input("Ten tap tin la: ")
    f = open(ten_tap_tin, 'w')
    f.write(n)
def main():
    exercises1()
if __name__=="__main__":
    main() 
