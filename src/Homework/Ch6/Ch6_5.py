def main():

    fileName = "numbers.txt"
    fileToRead = open(fileName, 'r')
    count = 0
    total = 0
    
    print('This will total the numbers in the file.')
    for line in fileToRead:        
        nums = int(line)
##        count += 1
        total += nums
    print('\nThe total is: ', total)
    
    fileToRead.close()
        
main()
