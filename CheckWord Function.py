def check_word(word, strn):
    found = True
    start = 0
    for ch in word:
        pos = strn.find(ch, start)
        if pos < 0:
            found = False
            break
        start = pos + 1
    if found:
        print("Yes, found.")
    else:
        print("No, not found.")


check_word('car', 'zxcasdef')
