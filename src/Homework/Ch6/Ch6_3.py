def inputFile():
    #print('<<<>>>', sep='',end='')
    filename = input("Enter the name of your file: ")
    return filename

def main():
    
    userFile = open(inputFile(), 'r')
    lineCount = 0;
    print()
    for line in userFile:
        stuff = line
        lineCount += 1
        print('Line ', lineCount,': ', stuff, sep='',end='')
    userFile.close()

main()
