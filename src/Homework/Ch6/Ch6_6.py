def main():

    fileName = "numbers.txt"
    fileToRead = open(fileName, 'r')
    count = 0
    total = 0
    
    print('This will total the numbers in the file.')
    for line in fileToRead:        
        nums = int(line)
        count += 1
        total += nums
    print('\nNumber of ints in file: ', count)
    print('The total is: ', total)
    print('The average is: ', format(total/count, ',.3f'))
    
    fileToRead.close()
        
main()
