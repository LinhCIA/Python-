from random import randint
def exercises5():
    x = [randint(-1000, 1000) for l in range(0, 1000)]
    print('Danh sach sinh ngau nhien la\n', x)
    ten_tap_tin = input("Ten tap tin la:")
    f = open(ten_tap_tin, "w",encoding='utf-8')
    y = []
    for i in range(10):
        y.append(i)
    for i in range(100):
        for j in range(10):
            y[j] = str(x[i * 10 + j])
        f.write(','.join(y) + "\n")
    f.close()
    with open(ten_tap_tin, "r+") as f:
        r = f.read()
        r = r.replace(",", "  ")
        print(r)
def main():
    exercises5()
if __name__=="__main__":
    main()