import pandas
import requests # importing the request module


url = 'https://the-internet.herokuapp.com/' # text from a website

response = requests.get(url) # opening a network and fetching a data
print(response)
print(response.status_code) # status code, success:200
print(response.headers)     # headers information
print(response.text) # gives all the text from the page

from mypackage import arithmetic
print(arithmetic.add_numbers(1, 2, 3, 5))
print(arithmetic.subtract(5, 3))
print(arithmetic.multiple(5, 3))
print(arithmetic.division(5, 3))
print(arithmetic.remainder(5, 3))
print(arithmetic.power(5, 3))

from mypackage import greet
print(greet.greet_person('Megan', 'M'))

import re
def most_frequent_words(txt):
    words = re.findall(r'\w+', txt, re.I)
    #print(words)
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    formatted_counts = [(count, word) for word, count in word_counts.items()]
    formatted_counts.sort(reverse=True)
    print(formatted_counts[:10])

url = "https://www.gutenberg.org/cache/epub/1513/pg1513-images.html"

response = requests.get(url)
print(most_frequent_words(response.text))


import json
import math
import statistics
URL = "https://api.thecatapi.com/v1/breeds"
API_KEY = "live_JIkaFt9gA0Gwbh3ZVmrAYjGAuRCNyDz17hnKDdLbTLdBGgVr9guWkAB5piIiiRF6"
headers = {"x-api-key": API_KEY}

response = requests.get(URL, headers=headers)
breeds = response.json()

weights = []
countries = {}
breeds_by_country = {}

for breed in breeds:
    weight = breed.get('weight').get('imperial')
    if weight:
        weight_range = [int(x.strip()) for x in weight.split("-")]
    for item in weight_range:
        weights.append(int(item))
    print(weight_range)
    print(breed.get('name'))
weights.sort()
print(f"Min weight: {min(weights)}\nMax weight: {max(weights)}\nMean weight: {sum(weights)/len(weights):.2f}\nMedian weight: {weights[len(weights)//2]}")

for breed in breeds:
    cat_country = breed.get("country_code")
    cat_name = breed.get("name")
    if cat_country:
        countries[cat_country] = countries.get(cat_country, 0) + 1
    if cat_country and cat_name:
        if cat_country not in breeds_by_country:
            breeds_by_country[cat_country] = []
        breeds_by_country[cat_country].append(cat_name)

print("\n--- Country Frequency Table ---")
for country, count in sorted(countries.items(), key = lambda x: x[1], reverse= True) [:5]:
    print(f"{country}: {count}")

print("\n--- Country Breed Frequency Table ---")
for country, breed in sorted(breeds_by_country.items(), key = lambda x: len(x[1]), reverse= True):
    #print(f"{country}: {breed}")
    breeds_str = ", ".join(breed)
    print(f"{country} ({len(breed)} breeds): {breeds_str}")