minimum = None
while True:
    n = input()
    if n == '.':
        break
    n = float(n)
    minimum = n if minimum is None or n < minimum else minimum

print(minimum)
