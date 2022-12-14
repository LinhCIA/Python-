def exercises2():
    #nhap ten tap tin tu ban phim
    ten_tap_tin = input("Ten tap tin la:")
    #doc noi dung tap tin va in ra man hinh
    with open(ten_tap_tin, 'r', encoding='utf-8') as f:
        read = f.read()
     print('doc tap tin:\n', read)
def main():
    exercises2()
if __name__=="__main__":
    main()
