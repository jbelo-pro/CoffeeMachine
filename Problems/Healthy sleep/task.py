a = int(input())
b = int(input())
h = int(input())


if h > b:
    print("Excess")
elif a <= h <= b:
    print("Normal")
else:
    print("Deficiency")
