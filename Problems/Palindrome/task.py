# put your python code here

word = input()

for p in range(0, int(len(word) / 2)):
    if word[p] != word[(p + 1) * -1]:
        print('Not palindrome')
        break
else:
    print('Palindrome')
