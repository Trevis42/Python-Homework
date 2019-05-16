days = int(input('Enter a number from 1-7:'))
while  days > 7 or days < 1:
    print('Error, bad input')
    days = int(input('Enter a number from 1-7:'))
#for days in range(1 - 8):
if days == 1:
    print('The day of the week is Monday.')
elif days == 2:
    print('The day of the week is Tuesday')
elif days == 3:
    print('The day of the week is Wednesday')
elif days == 4:
    print('The day of the week is Thursday.')
elif days == 5:
    print('The day of the week is Friday.')
elif days == 6:
    print('The day of the week is Saturday.')
elif days == 7:
    print('The day of the week is Sunday.')


    
