##loan payment, insurance, gas, oil, tires, maintenance: monthy
## monthly total and yearly total

def inputCosts():
    print("Enter the monthly costs for the following expenses"\
          "incured from operating your vehicle.\n")
    loan = float(input("Car loan:$ "))
    insurance = float(input("Car insurance:$ "))
    gas = float(input("Gas cost:$ "))
    oil = float(input("Oil cost:$ "))
    tires = float(input("Tire costs:$ "))
    maintenance = float(input("Maintenance cost:$ "))

    return loan, insurance, gas, oil, tires, maintenance

def calcMonthly(loan, insurance, gas, oil, tires, maintenance):
    return loan + insurance + gas + oil + tires + maintenance

def calcYearly(monthly):
    return monthly * 12

def displayCosts(monthly, yearly):
    print('\nTotal monthly cost:$', format(monthly, ',.2f'))
    print('Total annual cost:$',format(yearly, ',.2f'))

def main():
    loan, insurance, gas, oil, tires, maintenance = inputCosts()
    monthly = calcMonthly(loan, insurance, gas, oil, tires, maintenance)
    yearly = calcYearly(monthly)

    displayCosts(monthly, yearly)

main()
