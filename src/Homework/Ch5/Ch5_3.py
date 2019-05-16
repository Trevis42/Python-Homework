INSURE_PERCENT = .8

def userInput():
    return float(input("Enter property replacement value:"))

def calcMinCost(value):
    return value * INSURE_PERCENT

def displayResults(value, minCost):
    print("\nThe value of your property is:$", format(value,',.2f'),
          "\nAdvised insurance percentage:", format(INSURE_PERCENT * 100, '.2f'), "percent.",
          "\nThe minimum cost to insure the property is:$", format(minCost,',.2f'))

def main():
    value = userInput()
    minCost = calcMinCost(value)

    displayResults(value, minCost)

main()
    
