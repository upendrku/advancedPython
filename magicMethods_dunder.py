# Dunder -> starts with __
import datetime


# What is del in Python? In Python, the __del__() method is referred to as a destructor method.
# It is called after an object's garbage collection occurs,
# which happens after all references to the item have been destroyed.

# Python __len__() magic method
# It finally returns an integer value that is greater than or equal to zero as it represents the
# length of the object for which it is called.

# The __call__ method enables Python programmers to write classes where the instances behave like
# functions and can be called like a function.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is being deconstructed!")

    def __len__(self):
        return len(self.name)

    def __call__(self, *args, **kwargs):
        print("I was called")


p = Person("Mike", 25)
print(len(p))
p()


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __repr__(self):
        return f"X: {self.x}, Y: {self.y}"


v1 = Vector(10, 20)
v2 = Vector(50, 60)
# below will ot execute because python does not know how to add these and is not aware of vector type
# so need to add dunder add
v3 = v1 + v2
v4 = v1 - v2

print(v3)
print(v4)

# If both the functions return strings, which is supposed to be the object representation, what’s the difference?
# Well, the __str__ function is supposed to return a human-readable format,
# which is good for logging or to display some information about the object.
# Whereas, the __repr__ function is supposed to return an “official” string representation of the object,
# which can be used to construct the object again using eval function.
now = datetime.datetime.now()
now1 = eval(repr(now))
print(now == now1)
