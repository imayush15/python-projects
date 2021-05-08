import calendar

y = int(input("Enter Year : "))

print("\n(Enter the first 3 letters of month)")
m = input("Enter Month : ")

m1 = m.upper()

if m1 == 'JAN':
    m2 = 1
elif m1 == 'FEB':
    m2 = 2
elif m1 == 'MAR':
    m2 = 3
elif m1 == 'APR':
    m2 = 4
elif m1 == 'MAY':
    m2 = 5
elif m1 == 'JUN':
    m2 = 6
elif m1 == 'JUL':
    m2 = 7
elif m1 == 'AUG':
    m2 = 8
elif m1 == 'SEP':
    m2 = 9
elif m1 == 'OCT':
    m2 = 10
elif m1 == 'NOV':
    m2 = 11
else:
    m2 = 12
print('\n\n')
print(calendar.month(y, m2))