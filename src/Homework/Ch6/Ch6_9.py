def main():
    try:
        fileName = "numbers.txt"
        fileToRead = open(fileName, 'r')
        count = 0
        total = 0
        
        print('This will total the numbers in the file.\n')
        for line in fileToRead:        
            nums = int(line)
            count += 1
            total += nums

        fileToRead.close()
        
    except IOError as err:
        print(err)
        
    except ValueError as err:
        print(err)
    else:
        print('Number of ints in file: ', count)
        print('The total is: ', total)
        print('The average is: ', format(total/count, ',.3f'))
        
    finally:
        print('\nPlease come again.')

        
main()
