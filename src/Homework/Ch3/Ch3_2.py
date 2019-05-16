length1 = float(input('Enter the length of rectangle 1: '))
width1 = float(input('Enter the width of rectangle 1: '))

length2 = float(input('Enter the length of rectangle 2: '))
width2 = float(input('Enter the width of rectangle 2: '))

area1 = length1 * width1
area2 = length2 * width2
print('\nRect1 area:', area1,
      '\nRect2 area:', area2,)
if area1 == area2:
    print('\nThe areas of Rect1 and Rect2 are the same!')
elif area1 > area2:
    print("""\nRect1's area is greater.""")
else:
    print("""\nRect2's area is greater""")
