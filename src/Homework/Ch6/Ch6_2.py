def inputFile():
    filename = input("Enter the name of your file: ")
    return filename

def main():
    
    userFile = open(inputFile(), 'r')
    lineCount = 0
    print()
    while(lineCount < 5):
        stuff = userFile.readline()
        lineCount += 1
        print(stuff, end='')
        
    userFile.close()
    
main()
