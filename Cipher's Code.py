text = input("Enter your text: ")
shift = 0
while shift == 0:
    try:
        shift = int(input("Enter your shift value: "))
        if shift not in range(1, 26):
            raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Bad shift value!")
cipher = ''
for ch in text:
    if ch.isalpha():
        code = ord(ch) + shift
        if ch.isupper():
            f = ord('A')
        else:
            f = ord('a')
        code -= f
        code %= 26
        cipher += chr(code + f)
    elif ch.isdigit():
        ch = int(ch)
        ch = ch + shift
        ch = str(ch)
        cipher += ch
    else:
        cipher += ch
print(cipher)
