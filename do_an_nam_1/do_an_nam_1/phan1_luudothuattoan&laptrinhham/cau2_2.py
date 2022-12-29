# 2.Sắp xếp list các số thực ở trên theo chiều tăng dần (nếu tham số reverse= True), giảm dần(nếu tham số reverse= False)
def sap_xep_list_x_tang_dan(y):
    x1 = y.copy()
    for i in range(len(x1) - 1):
        for j in range(i + 1, len(x1)):
            if x1[i] > x1[j]:
                x1[i], x1[j] = x1[j], x1[i]
    return x1

def sap_xep_list_x_giam_dan(y):
    x2 = y.copy()
    for i in range(len(x2) - 1):
        for j in range((i + 1), len(x2)):
            if x2[i] < x2[j]:
                x2[i], x2[j] = x2[j], x2[i]
    return x2

def sap_xep(y, reverse):
    if reverse == True:
        return sap_xep_list_x_tang_dan(y)
    else:
        return sap_xep_list_x_giam_dan(y)
