def main():

    filename = 'numbers.txt'
    fileToRead = open(filename, 'r')
    count = 0
    total = 0
    
    print('This will total the numbers in the file.')
    for line in fileToRead:        
        nums = int(line)
        print(nums)
        count += 1
        total += nums
    print('\nNumber of random numbers:', count)
    print('The total is:', total)
    print('The average is: ', format(total/count, ',.3f'))
    
    fileToRead.close()
        
main()
