biggest = int(input())
smaller = int(input())
if smaller > biggest:
    biggest, smaller = smaller, biggest
print(biggest)
print(smaller)
