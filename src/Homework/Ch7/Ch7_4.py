MAX_SIZE = 20 #Set this to 20 because assignment asked for a series of 20 numbers
               #This wont change for now and makes code faster

def userInput(): #function for user input
    numsList = [] #creates new list
    for i in range(MAX_SIZE): 
        num = int(input('Enter numbers:'))
        numsList.insert(i,num) #adds each number at position i
    return numsList

def listTotal(nums):
    total = 0
    for n in nums:
        total = n + total #calculate total of each number
    return total

def listAvg(total, nums):
    return total/len(nums) #average = total/list size

def main():
    numbers = [] + userInput()

    print(numbers) #print the list
    print('\nLowest value Number:', min(numbers))
    print('Highest value Number:', max(numbers))
    print('Total:', listTotal(numbers))
    print('Average:', listAvg(listTotal(numbers), numbers))
    

# Call the main function.
main()
