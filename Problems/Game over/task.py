scores = input().split()
# put your python code here
i = 0
c = 0
for score in scores:
    if score == 'C':
        c += 1
    else:
        i += 1
    if i == 3:
        break

print('You won' if i < 3 else 'Game over')
print(c)
