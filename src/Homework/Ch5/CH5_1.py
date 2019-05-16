def userInput():
    km = float(input("Enter number of Kilometers to convert: "))
    return km

def convertToMiles(km):
    miles = km * 0.6214
    return miles

def main():
    kilometers = userInput()
    miles = convertToMiles(kilometers)
    print('\n')
    print(kilometers, "km =", format(miles,',.4f'), "mi")

main()
