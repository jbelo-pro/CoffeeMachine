
name = None
cats = 0
while True:
    cafe = input()
    if cafe == 'MEOW':
        break
    name_t = cafe[:cafe.find(' ')]
    number = int(cafe[cafe.find(' ') + 1:])
    if number >= cats:
        cats = number
        name = name_t
print(name)