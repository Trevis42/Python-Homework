#Exercise 4
speed = float(input('What is the speed of your vehcile?: '))
hours = float(input('How many hours has it travled?: '))
step = 0
print('Hour \t\tDistance Traveled')
print('---------------------------------')
while step < hours:
    distance = (step + 1) * speed
    print((step + 1), format(distance,'5.0f'), sep='\t\t\t')
    step += 1
