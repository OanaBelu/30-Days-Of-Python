import functools


# Day 29: Decorators

# Fundamentally, a decorator is just a function, or more generally a callable. We're going to focus on functions in
# this post, since they're the only callables we know about.
# Decorators are special functions, because they take in some other function and they give us back a new function
# which can do something more than the function we passed in
# Decorators are very useful, because they allow us to very easily provide some additional functionality to many
# functions in our application. Due to their power and flexibility, they're used quite extensively in both the standard
# library modules, and third party libraries.

def add(a, b):
    return a + b

# When we define a function like this, Python creates a function object which is a callable. In other words, we can
# the call the function using this object. This object is assigned to a variable with the same name as the function.

# Whenever we write add, we're just referencing this function object. This is just a value like any other,
# since functions are first class citizens in the Python language

# add and add() are both expressions, but the first evaluates to a function object, and the second evaluates to
# whatever the function returns when we call it.

# Let's start with an example which we can deconstruct in a moment.

from typing import Callable

def example_decorator(func: Callable) -> Callable:
    def inner():
        print(f"Now calling {func.__name__}...")
        func()
        print(f"{func.__name__} has ended.")

    return inner

# Starting with the top line, we can see that we have a single parameter in this case, which called func. As we've
# already discussed, we expect the argument passed to func to be a function.
# Now we get to the function body of example_decorator, and things get interesting. Inside the function body, we've
# defined a new function. This new function is called inner, and just to be clear, the name is not special.
# This inner function does a few things when it gets called.

# First it prints a line to the console, then it calls func, which is an alias for the function we passed into
# example_decorator, and then it prints another line to the console.
# In case you're wondering, the .__name__ is just an attribute which we can use to find the name of a function
# Note however, that we don't actually call inner. We've just defined this new function.
# After we're done defining inner, we return a reference to inner from example_decorator.

# To use the decorator, we can do something like this:
from typing import Callable

def example_decorator(func: Callable) -> Callable:
    def inner():
        print(f"Now calling {func.__name__}...")
        func()
        print(f"{func.__name__} has ended.")

    return inner

def greeter():
    print("Hello!")

# All the real action goes on on this line
greeter = example_decorator(greeter)
greeter()

# Here we've defined another function called greeter, which just prints "Hello!" to the console when we call it.

# The @ syntax
# Instead of doing this assignment, we can decorate a function by putting @ followed by the decorator name.
# This is placed right above the function we want to decorate.

# This is absolutely identical to what we did before:
from typing import Callable

def example_decorator(func: Callable) -> Callable:
    def inner():
        print(f"Now calling {func.__name__}...")
        func()
        print(f"{func.__name__} has ended.")

    return inner

@example_decorator
def greeter():
    print("Hello!")

greeter()

#  We therefore shouldn't do something like this:
from typing import Callable, Union

Real = Union[int, float]

def calculate(func: Callable) -> Callable:
    def inner(a, b):
        print("Calculating...")
        func(a, b)

    return inner

@calculate
def add(a: Real, b: Real):
    print(a + b)

add(1, 5)

# It works, but it only works when the function has two parameters. If we want to perform a unary operation, or we
# want to be able to decorate something like sum, we'd need a different decorator.
# Using *args and **kwargs we can accept any set of arguments we like for inner, and then we can pass them right along
# to the func.
from typing import Callable, Union

Real = Union[int, float]

def calculate(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("Calculating...")
        func(*args, **kwargs)

    return inner

@calculate
def add(a: Real, b: Real):
    print(a + b)

add(1, 5)

# If you need a refresher on *args and **kwargs, have another look at day 17.

# Decorating functions with return values
# we'll just return it inside of inner, but we don't do anything with this value. We don't pass that value on.
# Luckily this is a very easy one to solve: we just have to return the value from inner as well.
# For example, here is a very silly decorator which gives us the wrong answer for our calculations

from typing import Callable, Union

Real = Union[int, float]

def wrong_answer(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        return func(*args, **kwargs) + 1

    return inner

@wrong_answer
def add(a: Real, b: Real) -> Real:
    return a + b

print(add(1, 5))  # 7

# The wraps function
# One final thing I want to talk about in this post is a function in the standard library called wraps, which is in the
# functools module. We use wraps to decorate our inner functions, and its job is to preserve the original name of the
# function we passed into the decorator.
# If you remember back to our original example, referencing the variable name greeter gave us back something like this:
# <function example_decorator.<locals>.inner at 0x7f6e06326830>
# The name of our original greeter function is totally gone
# Using wraps, we can preserve the original function name, and importantly, any documentation included in that function.
# wraps is not strictly speaking a decorator: it's a decorator factory. That means it's a function that returns a
# decorator. This isn't a detail we need to worry about, but it does mean the syntax is slightly different, because
# wraps is able to take its own arguments.
# When we call wraps, we use the same @ syntax, and we pass in func as an argument. Here is an example:
from functools import wraps
from typing import Callable

def example_decorator(func: Callable) -> Callable:
    @wraps(func)
    def inner():
        print(f"Now calling {func.__name__}...")
        func()
        print(f"{func.__name__} has ended.")

    return inner

def greeter():
    print("Hello!")

greeter = example_decorator(greeter)
print(greeter)  # <function greeter at 0x0000020633FDA5C0>

# As you can see, the function we got back from example_decorator is still called greeter, despite us actually
# returning the inner function.

# A real world example:
# We're going to create a decorator that will time our code for us.
# In order to actually test our code, we're going to use the time module, which contains a function called perf_counter.
# perf_counter is going to give us a very detailed representation of the current time.

# By calling perf_counter, running our code, and calling perf_counter again, we can get a good idea of the time that
# elapsed between the two called to perf_counter

from functools import wraps
from time import perf_counter
from typing import Callable, List, Set

def stopwatch(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = perf_counter()
        func(*args, **kwargs)
        stop_time = perf_counter()

        print(f"{func.__name__} ran in {stop_time - start_time:.5f}s")

    return inner

@stopwatch
def make_list(size: int) -> List:
    return list(range(size))

@stopwatch
def make_set(size: int) -> Set:
    return set(range(size))

make_list(100_000)  # make_list ran in 0.00407s
make_set(100_000)   # make_set ran in 0.00628s

# The best way to do this would be using a decorator factory, which would allow us to pass in arguments to our
# decorator, but using our current knowledge, we can at least have the test run 10 times.
from functools import wraps
from math import fsum
from time import perf_counter
from typing import Callable, List, Set

def stopwatch(func: Callable) -> Callable:
    @wraps(func)
    def inner(*args, **kwargs):
        times = []

        for _ in range(10):
            start_time = perf_counter()
            func(*args, **kwargs)
            stop_time = perf_counter()

            elapsed = stop_time - start_time
            times.append(elapsed)

        average_time = fsum(times) / len(times)

        print(f"{func.__name__} ran in {average_time:.5f}s on average")

    return inner

@stopwatch
def make_list(size: int) -> List:
    return list(range(size))

@stopwatch
def make_set(size: int) -> Set:
    return set(range(size))

make_list(100_000)  # make_list ran in 0.00337s on average
make_set(100_000)   # make_set ran in 0.00565s on average

# Now our performance tests should see a lot less fluctuation, giving us a better picture of the performance differences

import functools

user = {"username": "Jose", "access_level": "admin"}
def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No admin permission for {user['username']} ."

        return secure_function

    return decorator()

@make_secure("admin")
def get_admin_pass():
    return "admin: 1234"

@make_secure("user")
def get_dashboard_pass():
    return "user: user_password"

# get_admin_pass = make_secure(get_admin_pass)

print(get_admin_pass())
print(get_dashboard_pass())


"""Exercises
Make a decorator which calls a given function twice. You can assume the functions don't return anything important, 
but they may take arguments.

Imagine you have a list called books, which several functions in your application interact with. Write a decorator 
which causes your functions to run only if books is not empty.

Write a decorator called printer which causes any decorated function to print their return values. If the return 
value of a given function is None, printer should do nothing."""










