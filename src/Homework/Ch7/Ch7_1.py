WEEK = 7

def userInput(): #function for user input
    salesList = [] #creates new list
    for i in range(WEEK):
        print('Enter sales for day', i+1,end=': ')
        sales = float(input(''))
        salesList.insert(i, sales) #adds each number at position i
    return salesList

def listTotal(sales):
    total = 0
    for s in sales:
        total = s + total #calculate total of each number
    return total

def main():
    print('**** Sales for the week ****\n')
    rainFall = [] + userInput()
    print('\nTotal Sales:$', format(listTotal(rainFall), '.2f'))

# Call the main function.
main()
