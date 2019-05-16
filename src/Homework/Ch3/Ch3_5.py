print ('\n** This program will allow you to find the weight(N)',\
      'of an object. **\n')
mass = float(input('Enter the mass(kg) of an object:'))
GRAVITY = 9.8

weight = mass * GRAVITY

print('Mass of the object:', format(mass,',.2f'), 'kgs',
      '\nGravity (constant):', GRAVITY, 'm/s^2',
      '\nWeight of the object:', format(weight,',.2f'), 'N')
if weight > 500:
    print('Object is too heavy!')
elif weight < 100:
    print('Object is too light!')
