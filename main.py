# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    ','.join(word)
    word = sorted(word)
    ','.join(anagram)
    anagram = sorted(anagram)
    if word == anagram:
        return True
    return False


print(find_anagrams("hello", "check"))
print(find_anagrams("below", "elbow"))
