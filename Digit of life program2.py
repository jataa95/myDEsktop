y = input("Enter your year of birth in the format-YYYY: ")
m = input("Enter your month of birth in the format-MM: ")
d = input("Enter your day of birth in the format-DD: ")
if len(y) != 4 or not y.isdigit():
    print("Invalid data input")
elif len(m) != 2 or not m.isdigit():
    print("Invalid data input")
elif len(d) != 2 or not d.isdigit():
    print("Invalid data input")
else:
    date = y + m + d
    while len(date) > 1:
        the_sum = 0
        for x in date:
            the_sum += int(x)
        print(date)
        date = str(the_sum)
    print('Your digit of life is: ' + date)
