from Ch11_1employee import Employee

class ShiftSupervisor(Employee):
    
    def __init__(self, name, idNum, salary, bonus):
        Employee.__init__(self, name, idNum)
        self.set_salary(salary)
        self.set_bonus(bonus)

    def set_salary(self, salary):
        self.__salary = salary
    def set_bonus(self, bonus):
        self.__yearlyBonus = bonus

    def get_salary(self):
        return self.__salary
    def get_bonus(self):
        return self.__yearlyBonus

    def __str__(self):
        str1 = "\n{0}\nSalary:{1}\nYearly Bonus:{2}".format(super().__str__(),
                                             self.get_salary(),
                                             self.get_bonus())
        return str1

def main():
    name, number, salary, bonus = userInput()
    shiftSup = ShiftSupervisor(name, number, salary, bonus)
    print(str(shiftSup))

def userInput():
    name = input("Enter the Employee's name: ")
    number = int(input("Enter Employee number: "))
    shift = float(input("Enter Salary: "))
    hourlypay = float(input("Enter annual production bonus: "))
    return name, number, shift, hourlypay

main()
