STATE_TAX = .05
COUNTY_TAX = .025

def state_and_countyTax(purchase):
    return purchase * STATE_TAX, \
           purchase * COUNTY_TAX

def taxTotal(sTax, cTax):
    return sTax + cTax

def totalCost(purchase, tax):
    return purchase + tax

def userInput():
    purchase = float(input('Enter your total purchase amount: '))
    return purchase

def displayResults(purchase, sTax, cTax, taxTotal, totalCost):
    print('\nYour purchase amount is: $', format(purchase, ',.2f'))
    print('State tax (5%) is: $', format(sTax, ',.2f'))
    print('County tax (2.5%) is: $', format(cTax, ',.3f'))
    print('\tTotal tax is: $', format(taxTotal,',.2f'))
    print('\tTotal after tax is: $', format(totalCost,',.2f'))
    print('\n')

def main():
    purchase = userInput()
    stateTax, countyTax = state_and_countyTax(purchase)
    tax = taxTotal(stateTax, countyTax)
    total = purchase + tax

    displayResults(purchase, stateTax, countyTax, tax, total)

main()
