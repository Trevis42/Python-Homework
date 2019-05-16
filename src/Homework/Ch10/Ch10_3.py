class Info:

    def __init__(self, name, address, age, number):
        self.__setName(name)
        self.__setAddress(address)
        self.__setAge(age)
        self.__setNumber(number)

    def __setName(self, name):
        self.__name = name
        
    def __setAddress(self,address):
        self.__address = address
        
    def __setAge(self, age):
        self.__age = age
        
    def __setNumber(self, number):
        self.__phoneNumber = number

    def getName(self):
        return self.__name
    def getAddress(self):
        return self.__address
    def getAge(self):
        return self.__age
    def getNumber(self):
        return __phoneNumber

def main():
    ##Assignment said to hold the data in three instances only.
    ##Does not say to use data or print it.
    p1 = Info('Trevor', '123 fake street', 31, "123-456-7890") #me (non-real info)
    p2 = Info('Lara', '123 fake street', 29, "321-654-0987")
    p3 = Info('Kevin', 'Somewhere in Utah', 29, "518-704-9632")

main()
