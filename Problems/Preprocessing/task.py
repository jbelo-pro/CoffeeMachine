t = input()

t = t.replace(',', '')
t = t.replace('.', '')
t = t.replace('!', '')
t = t.replace('?', '')

t = t.strip()
t = t.lower()
print(t)