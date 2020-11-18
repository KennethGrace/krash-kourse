#!/usr/bin/env python3

# Figure 3.1
def does_nothing():
    return 1

print(dir(does_nothing))
print(does_nothing)
print(does_nothing.__call__)
print(does_nothing())

# Figure 3.2
def ensure_integers(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
               return None
        return func(*args)
    return wrapper

def sum(a, b):
    return a + b

validating_sum = ensure_integers(sum)

print(validating_sum(1, 2))
print(validating_sum('bob', 3))
print(sum)
print(validating_sum)

# Figure 3.3
@ensure_integers
def sum(a, b):
    return a + b

print(sum)