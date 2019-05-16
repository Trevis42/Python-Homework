age = float(input('\t(** Please use decimal if under 1yr old **)\nEnter the age of the person:'))

if age >= 20:
    print('This person is an adult.')
elif age < 20 and age >= 13:
    print('This person is a teenager.')
elif age < 13 and age > 1:
    print('This person is a child.')
else:
    print('This person is an infant')
