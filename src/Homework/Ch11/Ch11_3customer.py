from Ch11_3person import Person

class Customer(Person):
    
    def __init__(self, fName, lName, address, telNum, customerId, mail):
        Person.__init__(self, fName, lName, address, telNum)
        self.set_customerId(customerId)
        self.set_mail(mail)

    def set_customerId(self, customerId):
        self.__customerId = customerId
    def set_mail(self, mail):
        self.__mailList = mail

    def get_customerId(self):
        return self.__customerId
    def get_mail(self):
        return self.__mailList

    def __str__(self):
        str1 = "\n{0}\nCustomer Num:{1}\nMailing List:{2}".format(super().__str__(),
                                             self.get_customerId(),
                                             self.get_mail())
        return str1
