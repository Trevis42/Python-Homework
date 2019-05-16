class Employee:

    def __init__(self, name, idNum):
        self.set_name(name)
        self.set_id(idNum)

    def set_name(self, name):
        self.__name = name
    def set_id(self, idNum):
        self.__id = idNum

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id

    def __str__(self):
        str1 = "Employee Name:{0}\nEmployee Number:{1}".format(self.get_name(),
                                 self.get_id())
        return str1
