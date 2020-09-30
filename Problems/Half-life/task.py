atoms = int(input())
resulting = int(input())
counter = 0
while atoms > resulting:
    atoms = atoms * 0.5
    counter += 1

print(counter * 12)
