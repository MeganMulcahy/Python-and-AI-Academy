lst = list()
lst = []

list('abc')
list({1 , 2, 3})

lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # list containing different data types

fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit, second_fruit, third_fruit, *rest = fruits 
#* bundles rest of items into a list called rest / def func(*args) packs multiple inputs into a single tuple so you can call any number of inputs

all_fruits = fruits[0:4] # it returns all the fruits
print(all_fruits)

# this will also give the same result as the one above
all_fruits = fruits[0:] # if we don't set where to stop it takes all the rest
orange_and_mango = fruits[1:3] # it does not include the first index
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # here we used a 3rd argument, step. It will take every 2cnd item - ['banana', 'mango']
print(all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
print(orange_and_lemon)

all_fruits = fruits[-4:] # it returns all the fruits
orange_and_mango = fruits[-3:-1] # it does not include the last index,['orange', 'mango']
orange_mango_lemon = fruits[-3:] # this will give starting from -3 to the end,['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # a negative step will take the list in reverse order,['lemon', 'mango', 'orange', 'banana']

print(all_fruits)
print(orange_and_mango)
print(orange_mango_lemon)
print("reversed: ", reverse_fruits)

does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False

fruits.append('apple')
print(fruits) 
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
fruits.remove('banana')
print("remove banana:", fruits)  # ['orange', 'mango', 'lemon', 'banana'] - this method removes the first occurrence of the item in the list
    
fruits.pop()
print("pop():", fruits)       # ['banana', 'orange', 'mango']
fruits.pop(0)
print("pop(0):", fruits)       # ['orange', 'mango']


lst = fruits.copy()
print("copy of fruits:", lst)  # ['orange', 'mango']

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print(positive_numbers + negative_numbers) # [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]
print(positive_numbers * 2)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
#extend returns None so printing print(list1.extend(list2)) will give None, instead to print without changing use the + operator
print(list1) # [1, 2, 3, 4, 5, 6]

#sort returns None so printing print(positive_numbers.sort(reverse=True)) will give None
positive_numbers.sort(reverse=True)
print("sort(reverse=True):",positive_numbers) # [5, 4, 3, 2, 1]
positive_numbers.sort()
print("sort():",positive_numbers) # [1, 2, 3, 4,
positive_numbers.reverse()
print("reversed:",positive_numbers) # [5, 4, 3, 2, 1]
print("sorted() method on reversed:", sorted(positive_numbers)) # [1, 2, 3, 4, 5]
print("unaltered reversed list after sorted():", positive_numbers) # [5, 4, 3, 2, 1]

companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(companies[3:])
print(companies[:-3])
mid = len(companies) // 2
companies.pop(mid) if len(companies) % 2 != 0 else [companies.pop(mid-1)] #removes middle or left item in even cases
# line below dosnt work: del is an action statement and needs to be alone
# del companies[mid] if len(companies) % 2 != 0 else [companies.pop(mid), companies.pop(mid-1)]
print(companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + (back_end)
print(full_stack)

reduxindex = full_stack.index('Redux') # 4
full_stack.insert(reduxindex + 1, 'Python')
full_stack[reduxindex+1:reduxindex+1] = ['Python', 'SQL', 'MongoDB'] #inserts inebtween in thisempty spot. second numver +x is how many after it replaces in that place
print(full_stack)