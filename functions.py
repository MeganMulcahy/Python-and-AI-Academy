def add_two_numbers(x, y):
    return x+y
def area_circle(radius):
    return 3.14*radius*radius
#use *arg when functiona ccepts a varying # of args in a list or set etc. it creates a tuple
def check_type(*args):
    print(f"Data: {args} | Type: {type(args)}")

# 1. Passing individual items
check_type(1, 2, 3)  # Output: Data: (1, 2, 3) | Type: <class 'tuple'>
# 2. Passing a single list
check_type([1, 2, 3]) # Output: Data: ([1, 2, 3],) | Type: <class 'tuple'>
# 3. Passing a single set
check_type({1, 2, 3}) # Output: Data: ({1, 2, 3},) | Type: <class 'tuple'>
def add_all_nums(*args):
    for item in args:
        if not isinstance(item, (int, float)):
            print("Invalid input")
            break
    return sum(args)
print(add_all_nums(1, 2.5, 3, 4.5)) 
def solve_quadratic_eqn(a,b,c):
    import cmath
    #cmath not just math bc it supports complex numbers like the imaginary numbers
    if a == 0:
        if b == 0:
            if c!=0:
                return () 
            else:
                ("Infinite solutions")
        else:
            return (-c /b,)

    #-b+-root(b^2-4ac) / 2a
    left = (-b + cmath.sqrt((b*b) - (4*a*c))) / 2*a
    right = (-b - cmath.sqrt((b*b) - (4*a*c))) / 2*a
    
    x1 = left.real if left.imag == 0 else left
    x2 = right.real if right.imag == 0 else right

    if x1 == x2:
        return (x1,)
    return (x1, x2)
print(solve_quadratic_eqn(1,6,9))
print(solve_quadratic_eqn(1,0,1))

def reverse_list(arraylist):
    for item in arraylist:
        print(arraylist[len(arraylist) - item])

reverse_list([1,2,3,4,5])

def cap_list(listy):
    #for item in range(len(listy)):
        #listy[item] = listy[item].capitalize()
    #return listy
    return [item.capitalize() for item in listy]

food_stuff = ['potato', 'tamato', 'Mango', 'milk']
food_stuff = cap_list(food_stuff)

def add_item(list, item):
    list.append(item)
    return list
print(add_item(food_stuff, 'Meat'))

def remove_item(list, item):
    if item in list:
        list.remove(item)
    return list
print(remove_item(food_stuff, "Milk"))

def display_info(name, role="Student"):
    print(name, "is a", role)

# Positional Call
display_info("Rahul", "Captain") 

# Default Call
display_info("Sneha")  # Automatically uses "Student"

# Keyword Call
display_info(role="Teacher", name="Mr. Sharma") 

x = 10  # Global Variable

def modify() -> None: # -> is type hint does nothing just shows what return type should be
    global x
    x += 10  # Modifies the global variable x

print(x)
modify()
print(x)  # Outputs 20

def factorial(n):
    if n < 0:
        return("Inproper")
    sum = 1
    for item in range(n):
        sum += sum*item
    return sum
print(factorial(10))

def is_empty(param)->bool:
    return True if not(param) else False
print(is_empty(""))          # Returns True (Empty string)
print(is_empty([]))          # Returns True (Empty list)
print(is_empty(None))        # Returns True (None value)
print(is_empty("Hello"))     # Returns False (Non-empty string)

#The single asterisk *args captures non-named arguments as a tuple (e.g., (1, 2, 3)). Tuples do not support text keys like args[key]
#Changing it to **args turns the inputs into a dictionary, allowing you to look up values using keys.
def show_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_args(fruit="apple", color="red")


text = "Code 2026!"
digits = list(filter(str.isdigit, text))   
print(digits)

def is_even(num):
    return num % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

# Extract even numbers
even_numbers = list(filter(is_even, numbers)) 
print(even_numbers)


ages = [14, 18, 22, 30, 16]
# lamda is used to make an inline function basically, used in filter to act as the function like add_ten = lambda x: x + 10
# lambda used in filter(), map(), or sorted()
adults = list(filter(lambda x: x >= 18, ages))


# The filter way
evens = list(filter(lambda x: x % 2 == 0, numbers))

# The list comprehension way (performs the same action)
evens = [x for x in numbers if x % 2 == 0]