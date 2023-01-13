# This below code is not the way we do it in python.
import time


def mydecorator(function):
    def wrapper():
        print("I am decorating your function!")
        function()

    return wrapper


def hello_world():
    print("Hello World!")


mydecorator(hello_world)()

print("///////////////////////////")


# We can use an elegant way
def mydecorator2(function):
    def wrapper(*args, **kwargs):
        print("I am decorating your function!")
        return_value = function(*args, **kwargs)
        return return_value

    return wrapper


@mydecorator2
def hello(person):
    print(f"Hello {person}")
    return f"Hello {person}!"


print(hello("Mike"))

print("///////////////////////////")


# Practical Example #1 - Logging
def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f" {fname} returned value {value} \n")
        return value

    return wrapper


@logged
def add(x, y):
    return x + y


print(add(10, 20))

print("/////////////////////")


# Practical Example #2 - Timing

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after - before} seconds to execute!")
        return value

    return wrapper


@timed
def myfunction(x):
    result = 1
    for i in range(1, x):
        result *= i
        return result


myfunction(90000)


# What is Python *args ? The special syntax *args in function definitions in python is used to pass a variable number
# of arguments to a function. It is used to pass a non-key worded, variable-length argument list.

def myFun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Next argument through *argv :", arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')


# What is Python **kwargs The special syntax **kwargs in function definitions in python is used to pass a keyworded,
# variable-length argument list. We use the name kwargs with the double star. The reason is that the double star
# allows us to pass through keyword arguments (and any number of them).
# A keyword argument is where you provide a name to the variable as you pass it into the function. One can think of
# the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we
# iterate over the kwargs there doesn’t seem to be any order in which they were printed out.

def myFun2(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun2(first='Geeks', mid='for', last='Geeks')
