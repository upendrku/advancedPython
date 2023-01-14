# within a class if we declare something with double underscore it counts as private variable

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.__age = age
        self.gender = gender

    @property
    def Age(self):
        return self.__age

    @Age.setter
    def Age(self, value):
        self.__age = value

    @staticmethod
    def mymethod():
        print("This function can be accesses directly from class")


p1 = Person("Mike", 20, 'M')
print(p1.name)
print(p1.Age)

p1.Age = 32
print(p1.Age)

Person.mymethod()
p1.mymethod()
