with open('./datafiles/example.txt', 'w') as f:
    f.write('This is an example to show how to open a file and read.\nThis is the second line of the text.\n')

# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
# "r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

f = open('./datafiles/example.txt')
print(f)

txt = f.read()
print(type(txt))
print(txt)

f.seek(0) # read moves the cursor so if you try to read the first 10 again it will read from the end of the file from the previous read

txt = f.read(10)
print(txt)

# readline()
f.seek(0)
line = f.readline()
print(line)

# readlines() returns a list of lines
f.seek(0)
lines = f.readlines()
print(lines)

# splitlines()
f.seek(0)
lines = f.read().splitlines()
print(lines)

f.close()

# with - automatically closes files after reading
with open('./datafiles/example.txt') as f:
    lines = f.read().splitlines()
    print(lines)

# a: appending to the end of files, if no file exists it creates a new one
# w: write, overwrites existing content, if no file exists it creates a new one
with open('./datafiles/example.txt', 'a') as f:
    f.write('This text has to be appended at the end')
    # print(f.read()) # you cant read() in a or w

with open('./datafiles/example.txt', 'w') as f:
    f.write('This text has to be appended at the end')
    # print(f.read()) # you cant read() in a or w

# print(f.read()) # file closed using `with`

import os
if os.path.exists('./files/exampleDNE.txt'):
    os.remove('./files/exampleDNE.txt')
else:
    print('The file does not exist')


# JSON
import json
with open('datafiles/persons.json', 'r') as file:
    person_dct = json.load(file)
print(person_dct)
print(person_dct['name'])

person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}

person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(person_json)

with open('./datafiles/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)


# CSV
import csv
with open('./datafiles/person.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are: {", ".join(row)}')
            line_count += 1
        else:
            print(
                f'{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')        


# XLSX - will cover in new file after pip
# import xlrd
# excel_book = xlrd.open_workbook('sample.xls')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)

def count_lines_and_words(filepath):
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
            linecount = len(lines)

            words = "".join(lines).split()
            wordcount = len(words)

            return linecount, wordcount
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        return 0,0

print(f"Number of lines: {count_lines_and_words('./datafiles/example.txt')[0]}, number of words: {count_lines_and_words('./datafiles/example.txt')[1]}")

# Unpack the returned tuple into 'lines' and 'words' variables
lines, words = count_lines_and_words('./datafiles/example.txt')

# Print the formatted text directly
print(f"Number of lines: {lines}, number of words: {words}")


def most_spoken_languages(filename, topn):
    if not os.path.exists(filename):
        return(f"Error: The file '{filename}' was not found.")
    
    with open(filename, 'r') as f:
        data = json.load(f)

    if not data:
        return(f"Error: The JSON file is empty.")
    
    languagecount = dict()
    for country in data:
        for language in country.get('languages', []):
            languagecount[language] = languagecount.get(language, 0) + 1

    sortedlanguages = sorted(languagecount.items(), key = lambda x: (x[1]), reverse = True)

    return [(count, language) for language, count in sortedlanguages[:topn]]

print(most_spoken_languages('./datafiles/country_data.json', 3))


def most_populated_country(filename, topn):
    if not os.path.exists(filename):
        return(f"Error: The file '{filename}' was not found.")
    
    with open(filename, 'r') as f:
        data = json.load(f)

    if not data:
        return(f"Error: The JSON file is empty.")
    
    popcount = dict()
    for country in data:
        popcount[country.get('name')] = country.get('population', 0)

    sortedpopulation = sorted(popcount.items(), key = lambda x: (x[1]), reverse = True)
    # returns dict, (country, count) sorted by dict[1] = value the count value

    return [
        {'country' : country, 'population': population} 
        for country, population in sortedpopulation[:topn]
    ]
print(most_populated_country('./datafiles/country_data.json', 3))


import re
def extract_emails(filename):
    if not os.path.exists(filename):
        return(f"Error: The file '{filename}' was not found.")

    email_list = []

    with open(filename, 'r') as f:
        # same as readlines() Danger: Loads whole file into memory at once
        for line in f:
            if line.startswith('From '):
                email = re.search(r'(\w+)+@[\w\.-]+', line)
                # print(email.group())
                if email:
                    email_list.append(email.group())
        return email_list
print(extract_emails('./datafiles/email_exchanges_big.txt'))

def find_most_common_words(filename, topn):
    if not os.path.exists(filename):
        return(f"Error: File at '{filename}' does not exist.")

    words_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.strip().lower().split()
            for word in words:
                words_dict[word] = words_dict.get(word, 0) + 1

    sorted_words = sorted(words_dict.items(), key = lambda x: x[1], reverse=True)

    return sorted_words[:topn]
print(find_most_common_words('./datafiles/sample.txt', 10))

print(find_most_common_words('./datafiles/romeo_and_juliet.txt', 10))


def clean_text(filepath: str):
    with open(filepath, "r") as f:
        rawtext = f.read().lower()
    return re.findall(r'\b[a-z]+\b',rawtext) # find only words (all are lower alr)

from datafiles.stop_words import stop_words as sw
def remove_support(all_words):
    return [word for word in all_words if word not in sw]

# print(remove_support(clean_text('./datafiles/sample.txt')))

def check_similarity(text1, text2):
    words1 = set(remove_support(clean_text(text1)))
    words2 = set(remove_support(clean_text(text2)))

    intersect = words1.intersection(words2)
    union = words1.union(words2)

    #print(intersect) # only matching
    #print('\n')
    #print(union) # all words
    return round(len(intersect)/len(union) , 2) if union else 0.0

print(check_similarity('./datafiles/michelle_obama_speech.txt', './datafiles/melina_trump_speech.txt'))

import csv
def count_languages(filepath):
    py_count = 0
    js_count = 0
    java_count = 0

    with open(filepath, 'r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            line = " ".join(row).lower()

            if "python" in line:
                py_count += 1

            if "javascript" in line:
                js_count += 1

            if "java" in line and "javascript" not in line:
                java_count += 1
    return f"Python count: {py_count}\nJavaScript count: {js_count}\nJava (not JS) count: {java_count}"
print(count_languages("./datafiles/hacker_news.csv"))