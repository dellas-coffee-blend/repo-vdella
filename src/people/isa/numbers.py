# coding=utf-8

def is_a_prime_number(number):
    contador = 2
    while contador != number:
        if number % contador == 0:
            return False
        contador = contador + 1
    return True


def fib(number):
    return number


def prime_number_fib(number):
    return number


def area(shape, *value_according_to_shape):
    return shape, value_according_to_shape


def sum_as_much_as_possible(*args):
    return args
