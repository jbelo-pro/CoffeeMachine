word = input()
new_word = ''

for c in word:
    n = c if c.islower() else '_' + c.lower()
    new_word = new_word + n

print(new_word)
