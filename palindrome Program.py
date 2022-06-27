def palindromeFunc(word):
    word = word.replace(' ', '')
    if len(word) > 1 and word.lower() == word[::-1].lower():
        print("It's a palindrome")
    else:
        print("It's not a palindrome")


palindromeFunc('Eleven animals I slam in a net')
