from Ch11_1employee import Employee

class ProductionWorker(Employee):

    def __init__(self, name, idNum, shift, pay):
        Employee.__init__(self, name, idNum)
        self.setShift(shift)
        self.setPay(pay)

    def setShift(self, shift):
        self.__shift = shift
    def setPay(self, pay):
        self.__pay = pay

    def getShift(self):
        return self.__shift
    def getPay(self):
        return self.__pay

    def __str__(self):
        #print(Employee)
        str1 = "\n{0}\nShift Number:{1}\nHourly Payrate:{2}".format(super().__str__(),
                                                                    self.getShift(),
                                                                    self.getPay())
        return str1


def main():
    name, number, shift, payrate = userInput()
    pWorker = ProductionWorker(name, number, shift, payrate)
    print(str(pWorker))

def userInput():
    name = input("Enter the Employee's name: ")
    number = int(input("Enter Employee number: "))
    shift = int(input("Enter Shift number: "))
    hourlypay = float(input("Enter hourly pay rate: "))
    return name, number, shift, hourlypay

main()
