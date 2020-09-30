# put your python code here
sum_numbers = []
squares = 0

while True:
    number = int(input())
    sum_numbers.append(number)
    squares += number ** 2
    if sum(sum_numbers) == 0:
        break

print(squares)
