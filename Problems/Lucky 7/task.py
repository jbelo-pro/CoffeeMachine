lines = int(input())

by_seven = []

for l in range(lines):
    n = int(input())
    if n % 7 == 0:
        by_seven.append(n)

for n in by_seven:
    print(n ** 2)
