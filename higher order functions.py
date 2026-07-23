# Function as a paramter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

# Function as a return value
def square(x):
    return x**2
def cube(x):
    return x**3

def higher_order_function(type):
    if type == 'square':
        return square
    if type == 'cube':
        return cube
    
result = higher_order_function('square')
print(result(3))
result = higher_order_function('cube')(3)
print(result)

# Python closures
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(3))
closure_result = add_ten()(3)
print(closure_result)

# Decorators
# first normal nested
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        return function().upper()
    return wrapper
g = uppercase_decorator(greeting)
print(g())
g = uppercase_decorator(greeting)()
print(g)
#same function with decorator
def uppercase_decorator(function):
    def wrapper():
        return function().upper()
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())

#Applying multiple decorators
def uppercase_decorator(function):
    def wrapper():
        return function().upper()
    return wrapper
def split_string_decorator(function):
    def wrapper():
        return function().split()
    return wrapper
@split_string_decorator
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())

# another example to show why we would use this
# wrapper function
def log_wrapper(func):
    def wrapper():
        print("Function is starting...")
        return func()
    return wrapper

# the normal manual ressigns and wraps every time
def buy_item(): return "Item bought"
def sell_item(): return "Item sold"

# You have to manually reassign or wrap every time
secure_buy = log_wrapper(buy_item)
secure_sell = log_wrapper(sell_item)
print(secure_buy())
print(secure_sell())
# V.S.
# the decorator way
@log_wrapper
def buy_item(): return "Item bought"
@log_wrapper
def sell_item(): return "Item sold"
print(buy_item())
print(sell_item())

