money = int(input())

animals = {'Sheep': 6769, 'Cow': 3848, 'Pig': 1296, 'Goat': 678, 'Chicken': 23}

animal = None
amount = None

if money >= 6769:
    animal, amount = "sheep", money // 6769
elif money >= 3848:
    animal, amount = "cow", money // 3848
elif money >= 1296:
    animal, amount = "pig", money // 1296
elif money >= 678:
    animal, amount = "goat", money // 678
elif money >= 23:
    animal, amount = "chicken", money // 23

if animal:
    animal = animal + 's' if amount > 1 and animal != 'sheep' else animal
    print(amount, animal)
else:
    print("None")
