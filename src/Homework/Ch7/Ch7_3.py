MONTHS = 12

def userInput(): #function for user input
    rList = [] #creates new list
    for i in range(MONTHS):
        print('Enter rainfall for month', i+1,end='')
        rainfall = float(input(': '))
        rList.insert(i,rainfall) #adds each number at position i
    return rList

def listTotal(rain):
    total = 0
    for r in rain:
        total = r + total #calculate total of each number
    return total

def listAvg(total, rain):
    return total/len(rain) #average = total/list size

def main():
    rainFall = [] + userInput()

    #print(rainFall) #print the list
    print('\nTotal for the year:', format(listTotal(rainFall), '.2f'))
    print('Average monthly rainfall:', format(listAvg(listTotal(rainFall), rainFall), '.2f'))
    print('Highest rainfall:', format(max(rainFall), '.2f'))
    print('Lowest rainfall:', format(min(rainFall), '.2f'))

# Call the main function.
main()
