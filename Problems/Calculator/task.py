# put your python code here
a = float(input())
b = float(input())
operator = input()

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*":
    print(a * b)
elif operator == "pow":
    print(a ** b)
else:
    if b == 0:
        print("Division by 0!")
    elif operator == "/":
        print(a / b)
    elif operator == "mod":
        print(a % b)
    else:
        print(a // b)
