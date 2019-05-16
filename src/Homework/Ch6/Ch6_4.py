def main():

    fileName = "names.txt"
    fileToRead = open(fileName, 'r')
    count = 0

    print()
    for line in fileToRead:        
        stuff = line
        count += 1       

    print('Number of names in file: ', count, end='')
    
    fileToRead.close()
        
main()
