# Functions inputs/functionality/output
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


# First class objects, cna be passed around as arguments e.g. int/string/float etc.

def calculate(calc_function, n1, n2):
    return calc_function(n1, n2)


result = calculate(add, 2, 3)
print(result)


# Nested functions
def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    nested_function()


outer_function()

# Python decorator function
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


def say_bye():
    print("Bye")


@delay_decorator
def say_greeting():
    print("How are you?")


say_hello()
say_bye()
say_greeting()
