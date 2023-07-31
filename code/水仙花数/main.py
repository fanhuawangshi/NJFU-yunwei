L = 100
b = 0
s = 0
g = 0
while L < 1000:

    b = L // 100
    s = (L - b * 100) // 10
    g = L - b * 100 - s * 10
    if L == (b ** 3 + s ** 3 + g ** 3):
        print('L=' + str(L))
    L += 1
