# python is dynamically typed which means variable types are defined during runtime and not before.
# we can define type, but it will just be as a comment that will hint that what type of value it accepts but
# still will not error if something else is passed, just like a comment.
# Do achieve type checking we need to use library mypy and then use mypy type_hinting.py to execute

def myfunction(num: int):
    print(num)


# myfunction("Hello!") -> this will give error


def myotherfunction(myparameter: int) -> str:
    return f"{myparameter} + 10"


def otherfuntion(otherparameter: str):
    print(otherparameter)


# otherfuntion(myotherfunction(20)) -> this will give error as otherfunction is accepting paramater
# with type string but we are passing a function


# After python 3.9 we can hint list as well

def somefunc(param: list[int]):
    return param[0]


print(f"{somefunc([1, 2, 3])}")
