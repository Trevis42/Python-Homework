print('\n*** Magic Dates ***\n')

print('Magic dates are dates where month * day = two digit year\n')

month = int(input('Enter a month (1 - 12):'))
day = int(input('Enter a day (1 - 31):'))
year = int(input('Enter a year (00 - 99):'))

print('\nDate entered:')
print(month, day, year, sep='/')

magic = month * day
if magic == year:
    print('This is a magic date.')
else:
    print('This is not a magic date.')
