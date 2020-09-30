# put your python code here
a = int(input())
b = int(input())
c = int(input())

desks = 0
for t in [a, b, c]:
    desks += t // 2 + t % 2

print(desks)