column = int(input())
row = int(input())

if row == 1 or row == 8:
    if 1 < column < 8:
        print(5)
    else:
        print(3)
elif 1 < row < 8:
    if 1 < column < 8:
        print(8)
    else:
        print(5)