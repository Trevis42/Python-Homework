def calFromFat(gramsFat):
    return gramsFat * 9

def calFromCarb(gramsCarb):
    return gramsCarb * 4

def inputCals():
    fats = int(input('Enter your number grams of fats: '))
    carbs = int(input('Enter your number of grams of carbs: '))
    return fats, carbs

def display(calsFat, calsCarb):
    print('Calories from fats:', calsFat)
    print('Calories from carbs:', calsCarb)

def main():
    fats, carbs = inputCals()

    display(calFromFat(fats), calFromCarb(carbs))

main()
