vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'

word = input()

for character in word:
    if character in vowels:
        print('vowel')
    elif character in consonants:
        print('consonant')
    else:
        break
