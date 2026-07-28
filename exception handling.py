# try:
#     code in this block if things go well
# except:
#     code in this block run if things go wrong
import datetime
try:
    print(10 + '5')
except:
    print('Something went wrong')

'''try:
    name = input('Enter your name:')
    year_born = int(input('Year you were born:'))
    age = datetime.datetime.now().year - year_born
    print(f'You are {name}. And your age is {age}.')
except ValueError:
    print('Please enter a valid number for the year.')
except Exception as e:
    print(f'Something went wrong: {e}')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
'''

# Unpacking lists
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e
# takes 5 args

lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
print(sum_of_five_nums(*lst))


numbers = range(2, 7)
print(list(numbers)) # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
# same as
print(unpacking_person_info(dct['name'], dct['country'], dct['city'], dct['age']))

# Packing lists
def sum_all(*args):
    s = 0
    for i in args:
        s+=1
    return s
print(sum_all(1, 2, 3))
print(sum_all(1, 2, 3, 4, 5, 6, 7))

# Packing Dictionaries
def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250)

# Spreading
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)

# Enumerate
for index, item in enumerate([20, 30, 40]):
    print(index, item)

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')

# Zip
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})
print(fruits_and_veges)

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
es = [country for country in names if country == 'Estonia']
ru = [c for c in names if c == 'Russia']
nordic_countries = [c for c in names if c not in ('Estonia', 'Russia')]
print(es)
print(ru)
print(nordic_countries)
es = list(filter(lambda x: x == 'Estonia', names))
ru = list(filter(lambda c: c == 'Russia', names))
nordic_countries = list(filter(lambda c: c not in ('Estonia', 'Russia'), names))
print(es)
print(ru)
print(nordic_countries)