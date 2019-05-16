#Exercise 7
print('+--- Your salay: Number Pennies doubled each day ---+')
numPen = 1
CENTS = .01
days = int(input('\nHow many days would you like to be paid? '))
step = 0
total = 0
print('\n\tSalary(in cents):',' Days worked:', sep='\t    ')
print('--------------------------------|--------------------------')
while step < days:
    print(format((numPen * CENTS),'30,.2f'),format((step+1),'10.0f'), sep='\t|\t')
    total += numPen * CENTS
    numPen *= 2
    step += 1
print('\nTotal salary:$',format(total,'20,.02f'))
