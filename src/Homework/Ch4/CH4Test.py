posNum = int(input('Enter a nonzero number: '))

while posNum <= 0:
    print('Error: invalid input!')
    posNum = int(input('Enter a nonzero number: '))

print('\nYour number was:', posNum)
