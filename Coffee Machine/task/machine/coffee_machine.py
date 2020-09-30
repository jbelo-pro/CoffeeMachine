# Write your code here
t = ["Starting to make a coffee",
     "Grinding coffee beans",
     "Boiling water",
     "Mixing boiled water with crushed coffee beans",
     "Pouring coffee into the cup",
     "Pouring some milk into the cup",
     "Coffee is ready!"]

for i in t:
   print(i)

coffe_cups = int(input('Write how many cups of coffee you will need :'))
ingredients = {'water': 200, 'milk': 50, 'coffee beans': 15}
units = {'water': 'ml', 'milk': 'ml', 'coffee beans': 'g'}
print(f'For {coffe_cups} cups of coffee you will need:')
for k, v in ingredients.items():
     print('{} {} of {}'.format(v * coffe_cups, units[k], k))
