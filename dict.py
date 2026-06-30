empty_dict = {}
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

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

# dict len counts number of 'key: value' pairs
print(len(person))

#accessing items
print(person['name'])
print(person['address'])
print(person['skills'])
print(person['skills'][0])  # JavaScript
print(person['address']['street'])

#accesing not exisitng keys returns error so use get() to check if key exists and returns it or None instead of error
print(person.get('name'))
print(person.get('address'))
print(person.get('skills'))
print(person.get('skills')[0])
print(person.get('address'))
print(person.get('address').get('street'))

#add/modifyitems to dict
person['city'] = 'dallas'
print(person)
person['skills'].append('HTML')

#items() makes into a list of tuples dict_items[(key, value), (key, value)]
print("\nperson items: ", person.items())
for key, value in person.items():
    print(f"{key}: {value}")

#in to see if key exists in the dic
print('key2' in person)
print('name' in person)
print('Megan' in person) #not values

#removing key and value pairs
city = person.pop('city')
print(city)

print(f"\n{person}")
person['address'].pop('zipcode')
print(f"\n{person.get('address')}")

person.popitem()
print(f"\n{person}")

#copy dict
newbie = person.copy()

person.clear()
del person

# print(person) # Error doesnt exist
print(newbie)

#get keys and values
keys = newbie.keys()
values = newbie.values()
print(f"\n{keys}")
print(f"\n{values}")