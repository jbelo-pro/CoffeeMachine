# Save the input in this variable
ticket = input()

# Add up the digits for each half
half1 = 0
for c in ticket[:3]:
    half1 += int(c)

half2 = 0
for c in ticket[3:]:
    half2 += int(c)


# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")