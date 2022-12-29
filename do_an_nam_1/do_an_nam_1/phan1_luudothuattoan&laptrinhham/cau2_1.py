# 1.Sinh ngẫu nhiên các giá trị cho 1 list các số thực trong khoảng [a, b];
import random as r

r.seed(100)

def sinh_ngau_nhien(a):
    x = [r.uniform(-10, 10) for i in range(a)]
    return x
