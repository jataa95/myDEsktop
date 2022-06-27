word_one = input("Enter your first word: ")
word_two = input("Enter your second word: ")

if len(word_one) < 1 or len(word_two) < 1:
    print('No, not anagrams')
else:
    word_one = sorted(word_one.lower().replace(' ', ''))
    word_two = sorted(word_two.lower().replace(' ', ''))
    if word_one == word_two:
        print('Yes, anagrams.')
    else:
        print('No, not anagrams.')
