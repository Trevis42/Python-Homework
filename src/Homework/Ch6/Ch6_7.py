import random

def randNums():
    return random.randrange(1,500)
def userInput():
    return int(input('How many random numbers do you want? '))

def main():
    filename = 'random_nums.txt'
    nums = userInput()

    random_nums = open(filename, 'w')

    for count in range(1, nums + 1):
        randNum = randNums()

        random_nums.write(str(randNum) + '\n')

    random_nums.close()
    print('Data written to', filename)

main()
