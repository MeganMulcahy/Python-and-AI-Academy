# [expression for i in iterable if condition]
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

lst = [i for i in language]
print(type(lst))
print(lst)

numbers = [i for i in range(100)]
print(numbers)

squares = [i*i for i in range(11)]
print(squares)

#making a list of tuples
numbers = [(i, i*i) for i in range(11)]
print(type(numbers))
print(numbers)

even_numbers = [i for i in range(21) if i%2==0]
print(even_numbers)

odd_numbers = [i for i in range(21) if i%2!=0]
print(odd_numbers)

numbers = list(range(-8,10))
print(numbers)

list_of_lists = [[1,2,3],[4,5,6], [7,8,9]]
flatten_list = [number for row in list_of_lists for number in row]
print(flatten_list)

# long form
flatten_list = []
for row in list_of_lists:
    for number in row:
        flatten_list.append(number)
        print(flatten_list)

# LAMBDA
# create a lambda function: use lambda followed by parameters, followed by the expression
# it explicitly returns the expression

# syntax
def add_two_nums(a,b):
    return a+b
print(add_two_nums(2,3))
#lambda version
add_two_nums = lambda a,b: a+b
print(add_two_nums(2,3))

word1 = "abc"
word2 = "pbqdc"
for c1 in zip(word1, word2):
    print(c1)
for c1, c2 in zip(word1, word2):
    print(c1, c2)
    print(c1+c2)

square = lambda x: x ** 2
print(square(3))

multiple_variables = lambda a,b,c: a**2 - 3*b +4*c
print(multiple_variables(5,5,3))

def power(x):
    return lambda n : x ** n
# cube = power(5)(3) = (lambda n : 5 ** n) (3) = 5 ** 3
cube = power(5)(3)
print(cube)

# filter only neg. and zero in the list
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
posatives = [i for i in range(len(numbers)) if i > 0]
print(posatives)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = [number for row in list_of_lists for number in row]
print(flatten_list)

tuple_squares = [(i, i**0, i**1, i**2) for i in range(3)]
print(tuple_squares)
tuple_squares = [tuple([i]+[i**p for p in range(6)]) for i in range(6)]
print(tuple_squares)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_list = [(country, country[:3], capital) for sublist in countries for country, capital in sublist]
print(countries_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [{'country': country, 'city': capital} for sublist in countries for country, capital in sublist]
print(output)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [(first + " " + last) for sublist in names for first, last in sublist]
print(output)

solve_linear = lambda x1, y1, x2, y2, mode = "slope" : (y2-y1) / (x2-x1) if mode == "slope" else y1 - ((y2 - y1) / (x2 - x1)) * x1
slope = solve_linear(1, 2, 4, 14, mode="slope")
intercept = solve_linear(1, 2, 4, 14, mode="intercept")
print(f"Slope: {slope}")  # Output: Slope: 4.0
print(f"Y-Intercept: {intercept}")  # Output: Y-Intercept: -2.0
