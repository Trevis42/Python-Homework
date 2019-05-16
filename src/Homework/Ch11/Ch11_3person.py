class Person():
    def __init__(self, fName, lName, address, telNum):
        self.set_fName(fName)
        self.set_lName(lName)
        self.set_address(address)
        self.set_number(telNum)

    def set_fName(self, fName):
        self.__firstName = fName
    def set_lName(self, lName):
        self.__lastName = lName
    def set_address(self, address):
        self.__address = address
    def set_number(self, telNum):
        self.__telNumber = telNum

    def get_fName(self):
        return self.__firstName
    def get_lName(self):
        return self.__lastName
    def get_address(self):
        return self.__address
    def get_telNum(self):
        return self.__telNumber

    def __str__(self):
        str1 = "First name: {0}\nLast Name: {1}\nAddress: {2}\nTelephone Number: {3}".format(self.get_fName(),
                                                                                        self.get_lName(),
                                                                                        self.get_address(),
                                                                                        self.get_telNum())
        return str1
