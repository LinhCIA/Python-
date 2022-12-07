#Ý 1:
def ham1():
    f1 = open("C:/data/vb.txt", "r", encoding='utf-8')
    print(f1)
#Ý 2:
def ham2():
    f2 = open("C:/data/vb.txt", "w", encoding='utf-8')
    print(f2)
#Ý 3:
def ham3():
    f3 = open("C:/data/vb.txt", "r+b")
    print(f3)
#Ý 4:
def ham4():
    f4 = open("C:/data/vb.txt", "r", encoding='utf-8')
    print(f4)
#Ý 5:
def ham5():
    f5 = open("C:/vb.txt", encoding='utf-8')
    f5.close()
#Ý 6:
def ham6():
    try:
        f6 = open("C:/data/vb.txt", "r", encoding='utf-8')
        f6.read()
    finally:
        f6.close()
#Ý 7:
def ham7():
    with open("C:/data/vb.txt") as f:
        f.read()
        f.close()
#Ý 8:
def ham8():
    with open("C:/data/file.txt", "w", encoding='utf-8') as f:
        f.write('Linh dep trai\n')
        f.write('Cần tìm người yêu\n')
        f.write('Vui lòng liên hệ tôi')
        f.close()
#Ý 9 :
def ham9():
    with open("C:/data/vb.txt", "r", encoding='utf-8') as f:
        print(f.read())
        f.close()
def ham10(): #Ý 10
    with open("C:/Ảnh/LinhTop1.JPG", "rb") as f:
        print(f.read())
def main():
    ham1()
    ham2()
    ham3()
    ham4()
    ham5()
    ham6()
    ham7()
    ham8()
    ham9()
    ham10()
if __name__=="__main__":
    main()