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

