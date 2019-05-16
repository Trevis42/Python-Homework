##Assessment value .6 of property value
##property tax .72 per $100 of assessment value

ASSESSMENT = .6
TAX =.72

def calcAssessment(propVal):
    return propVal * ASSESSMENT

def calcTax(assessVal):
    return (assessVal / 100) * TAX

def inputPropVal():
    return float(input('Enter your property\'s value: '))

def main():
    assessmentValue = calcAssessment(inputPropVal())
    print('Assessment:$', format(assessmentValue, ',.2f'))
    propTax = calcTax(assessmentValue)
    print('Property Tax:$', format(propTax, ',.2f'))

main()
