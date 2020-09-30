numbers = [int(x) for x in input().split()]
t = 0
for n in numbers:
    t = t + n
print(t / len(numbers))
