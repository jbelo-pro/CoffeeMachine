# put your python code here
a = int(input())
b = int(input())
r = [x for x in range(a, b+1) if x % 3 == 0]
s = 0
for n in r:
    s += n
print(s / len(r))
