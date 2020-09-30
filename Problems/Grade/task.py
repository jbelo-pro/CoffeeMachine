student = int(input())
maximum = int(input())
percentage = student / maximum

if 0.90 <= percentage <= 1:
    print("A")
elif 0.80 <= percentage < 0.90:
    print("B")
elif 0.70 <= percentage < 0.80:
    print("C")
elif 0.60 <= percentage < 0.70:
    print("D")
else:
    print("F")