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

# map(function, iterable)
numbers = [1,2,3,4,5] # iterable
def square(x):
    return x ** 2

numbers_squared = [square(i) for i in numbers]
print(numbers_squared)

numbers_squared = map(square, numbers)
print(list(numbers_squared))

numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))

# Why it matters: It computes values on demand instead of loading everything into memory at once.
# Example: If you have 10 million items, map() consumes almost zero memory upfront, whereas a list comprehension will instantly allocate memory for all 10 million elements.

numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
upper_names = map(lambda x: x.upper(), names)
print(list(upper_names))

# filter(function, iterable)
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(x):
    if x % 2 == 0:
        return True
    return False

evennums = filter(is_even, numbers)
print(list(evennums))

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))

# reduce(function, iterable)
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
# reduce passes the running total into the first arg x
print(total)


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# all 3 take a function and an iterable.
# map: applied the function to each item in the iterable and returns an object
# filter: filters each item in the iterable for the function equals True and reutns an object
# reduce: combines each item in the iterable using the function and reutnrs a single value

# higher order funtion: function that accepts or returns another function
# closure: function that remembers variables from its outer scope even after that outer scope finishes executing
#          when a nested function references variables from its enclosing (outer) function, and the outer function returns that nested function.
# decorator: : A specific type of higher-order function that modifies the behavior of another function without changing its source code

country_upper = map(lambda x: x.upper(), countries)
print(list(country_upper))

countries_no_land = filter(lambda x: 'land' not in x, countries)
print(list(countries_no_land))

countries_no_begin_e = filter(lambda x: x[0].lower() != 'e', countries)
print(list(countries_no_begin_e))

all_countries = ", ".join(countries)
print(all_countries)
# Reduce joins items with commas, adding ", and " before the last element
all_countries = reduce(
    lambda x, y: (x + " and " + y) if y == countries[-1] else (x+ ", "+y), 
    countries
) + " are north European countries"
print(all_countries)

def categorize_countries(countries, pattern) -> list:
    return list(filter(lambda x: pattern.lower() in x.lower(), countries))

print(categorize_countries(countries, 'land')) 
print(categorize_countries(countries, 'stan')) 
print(categorize_countries(countries, 'ia'))   

# normal way counting and dicts
def count_country_letters(countries_list) -> dict:
    counts = {}
    for country in countries_list:
        letter = country[0].upper()
        counts[letter] = counts.get(letter, 0) + 1
    return counts
print(count_country_letters(countries))
# using map and filter
def count_country_letters(countries_list) -> dict:
    letters = {
            c[0].upper(): sum(1 for country in countries_list if country.upper() == c.upper()) for c in countries_list
            }
    print(letters)
count_country_letters(countries)

from datafiles.countries_data import countries

def get_frist_ten(countries_list) -> list:
    return [country['name'] for country in countries_list[:3]]
print(get_frist_ten(countries))

def sort(countries_list):
    by_name = sorted(countries_list, key = lambda x: x['name'])
    by_capital = sorted(countries_list, key = lambda x: x['capital'])
    by_pop = sorted(countries_list, key = lambda x: x['population'])
    print([country['name'] for country in by_name[:3]])
    print([country['name'] for country in by_capital[:3]])
    print([country['name'] for country in by_pop[:3]])

    lang_count = {}
    for country in countries_list:
        for lang in country['languages']:
            lang_count[lang] = lang_count.get(lang, 0) + 1
    print(sorted(lang_count, key = lambda list: list[1])[:3])
    # lambda list: list is key, value and we want the value
sort(countries)