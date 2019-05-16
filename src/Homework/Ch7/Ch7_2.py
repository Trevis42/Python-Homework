import random

def randNums(): #function for user input
    lotto = [] #creates new list
    for n in range(7):
        randNum = random.randrange(0,10)
        nums = randNum
        lotto.insert(n,nums) #adds each number at position i
    return lotto

def listTotal(number):
    total = 0
    for n in number:
        total = n + total #calculate total of each number
    return total
def displayNums(lotto):
    print('Lottery Number: ', end='')
    for nums in lotto:
        print(nums, end='')

def main():
    lotteryNums = [] + randNums()
    displayNums(lotteryNums)

# Call the main function.
main()
