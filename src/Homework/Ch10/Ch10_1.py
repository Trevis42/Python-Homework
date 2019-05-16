class Pet:

    def __init__(self, name, animalType, age):
        ##Using set methods to initialize the data.
        self.__set_name(name)
        self.__set_animal_type(animalType)
        self.__set_age(age)

    ##Mutators
    def __set_name(self, name):
        self.__name = name

    def __set_animal_type(self, animalType):
        self.__type = animalType

    def __set_age(self, age):
        self.__age = age
        
    ##Accessors
    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__type
    
    def get_age(self):
        return self.__age

    def __str__(self):
        return "Pet's name: {0}\nAnimal Type: {1}\nPet's age: {2}".format(self.get_name(),
                                                                                self.get_type(),
                                                                                self.get_age())

def main():

    name = input('Enter pet name: ')
    aType = input('Enter type of animal: ')
    age = int(input('Enter age of your pet: '))

    # Create an instance of the CellPhone class.
    pet = Pet(name, aType, age)

    print('\nPet Name:', pet.get_name())
    print('Type of animal:', pet.get_type())
    print('Pet age: ', pet.get_age())

    
main()
