list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 20]
for i in list:
    for j in list:
        for k in list:
            if i + j + k == 30:
                print(i, j, k)
