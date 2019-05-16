class Employee:

    def __init__(self, name, idNum, department, jobTitle):
        self.set_name(name)
        self.set_id(idNum)
        self.set_department(department)
        self.set_job(jobTitle)

    def set_name(self, name):
        self.__name = name
    def set_id(self, idNum):
        self.__id = idNum
    def set_department(self, dept):
        self.__department = dept
    def set_job(self, title):
        self.__jobTitle = title

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_department(self):
        return self.__department
    def get_job(self):
        return self.__jobTitle

    def __str__(self):

        str1 = "{0}\t{1}\t\t{2}\t{3}".format(self.get_name(),
                                                 self.get_id(),
                                                 self.get_department(),
                                                 self.get_job())
        return str1


def main():

    e1 = Employee('Susan Meyers','47899', 'Accounting', 'Vice President')
    e2 = Employee('Mark Jone', '39119','IT', '\tProgrammer')
    e3 = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')

    print('Name','\tID Number', 'Department', 'Job Title', sep='\t')
    print('=================================================================')
    print(str(e1), str(e2), str(e3), sep='\n')
    
main()
