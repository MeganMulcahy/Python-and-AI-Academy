language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

#String looping
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)

#Tuple looping
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

#Dict looping
person = {
    'name': 'Megan', 
    'age': 5, 
    'country': 'USA', 
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space Street', 
        'zipcode': '02210'
    }
}

print("\nKey in Person:")
for key in person:
    print(key)
    print(person[key])
    #print(value)  # This will raise an error because 'value' is not defined in this context

print("\nValues in Person:")
for value in person:
    print(value)
    #print(person[value])  # This will raise an error because 'value' is not a key in the dictionary

print("\nKey-Value pairs in Person:")
for key, value in person.items():
    print(f"{key}: {value}")
    print(value)
    print(person[key])

#Breaks to end and continue to skip
print("\nBreak and Continue Example:")
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    if number == 4:
        break
print('outside the loop')

print("Range Example:")
lst = list(range(11))
print(lst)
st = set(range(1,11))
print(st)

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# for backward from start to end 
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]

print("\nFor loop with range to 11:")
for number in range(11):
    print(number)   # prints 0 to 10, not including 11

print("\nFor loop with else:")
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)

print("\nFor loop with pass:")
for number in range(6):
    pass

print("\nGetting item in range:")
last_item = range(11)[0]
print(last_item)  # Outputs: 0
last_item = range(1, 11)[0]
print(last_item)  # Outputs: 1
last_item = range(1, 11)[-1]
print(last_item)  # Outputs: 10

for number in range(6):
    #print("#" * number)
    #print(2*number-1) # as number = 1, 2*1-1 = 1, 2*2-1 = 3, etc.
    print(" " * (6 - number) + "#" * (2 * number - 1))

for number in range(6):
    print(f"{number} x {number} = {number * number}")

list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for item in list:
    print(item)

for num in range(1,10,2):
    print(num)  # This will raise an error because 'int' object is not iterable

for num in range(9,0,-2):
    print(num) 

sum = 0
sumeven = 0
sumodd = 0
for num in range(0,101):
    sum += num
    if num % 2 == 0:
        sumeven += num
    else:
        sumodd += num
print("The sum is:", sum)
print("The sum of even numbers is:", sumeven)
print("The sum of odd numbers is:", sumodd)

from datafiles.countries_data import countries

unique_languages = set() #bc sets dont keep duplicates!
for country in countries:
    unique_languages.update(country['languages']) #update() adds elements to a set, but only if they are not already present
print("# of Unique languages:", len(unique_languages))

print("10 Most Popular Languages:")
language_counts = {}
for country in countries:
    for language in country['languages']:
        language_counts[language] = language_counts.get(language, 0) + 1 # This avoids key errors by safely setting a language's count to 0 the first time it is found before adding 1
sorted_languages = sorted(language_counts.items(), key=lambda item: item[1], reverse=True) # tells Python to sort the items based on their counts (the numbers) instead of their names (the text),
print("Most spoken languages:")
for language, count in sorted_languages[:10]:
    print(f"{language}: {count} countries")
    
print("10 Most Populated Countries:")
sorted_pop = sorted(countries, key = lambda country: country['population'], reverse=True)
for country in sorted_pop[:10]:
    print(f"{country['name']}: {country['population']}")
