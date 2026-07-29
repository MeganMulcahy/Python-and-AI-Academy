import re

# RedEx is a special text string that helps find patterns in data
# A RegEx can be used to check if some pattern exists in a different data type.

# Match
# re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore

txt = 'I love to teach python and javaScript'
match = re.match('I love to teach', txt, re.I)
print(match)
# We can get the starting and ending position of the match as tuple using span
span = match.span() # returns a tuple
print(span)
# Lets find the start and stop position from the span
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)
substring = txt[slice(*span)]
print(substring)
print(slice(*span))

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)

# Search
# re.search(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag

txt = "Python is the most beautiful language that a human being has ever created.\
I recommend python for a first programming language"

match = re.search('first', txt, re.I)
print(match) # It returns an object with span and match
span = match.span()
print(span)
start, end = span
print(start, end)
substring = txt[start:end]
print(substring)

# Searching for All Matches Using findall
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches) # It return a list ['language', 'language']

matches = re.findall('python', txt, re.I)
print(matches)

# Since we are using re.I both lowercase and uppercase letters are included. If we do not have the re.I flag, then we will have to write our pattern differently
# | OR operator
# Pp]ython
matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

# Replacing a substring
match_replaced = re.sub('Python|python', 'JavaScript', txt)
print(match_replaced)
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt)
print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''
matches = re.sub('%', '', txt)
print(matches)

# Splitting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))

# Writing RegEx Patterns
regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)

matches = re.findall(regex_pattern, txt, re.I)
print(matches)

regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
matches = re.findall(regex_pattern, txt)
print(matches)  

# Square Brackets: Include lower and upper case
regex_pattern = r'[Aa]pple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[Aa]pple|[Bb]anana'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)

# Escape characters (\)
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# One or more times(+)
regex_pattern = r'\d+'  # d+ to match one or more numbers together as a full group.
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# Period(.). means any character except new line
regex_pattern = r'[a].'  # this square bracket means a and the next letter other than a new line
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . any character, + any character one or more times
matches = re.findall(regex_pattern, txt)
print(matches)

# Zero or more times(*)
regex_pattern = r'[a].*'  # . any character, * any character zero or more times
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)

# Zero or one time(?)
regex_pattern = r'[Ee]-?mail'  # ? means here that '-' is optional
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
matches = re.findall(regex_pattern, txt)
print(matches)

# Quantifier in RegEx
regex_pattern = r'\d{4}'  # exactly four times
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'\d{1,4}'
txt = 'This regular expression example was made on December 26,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches) 

# Cart ^
regex_pattern = r'^This'  # ^ means starts with
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)

# What is the most frequent word in the following paragraph?
paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."
def most_frequent_words(txt):
    words = re.findall(r'\w+', txt, re.I)
    print(words)
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    formatted_counts = [(count, word) for word, count in word_counts.items()]
    formatted_counts.sort(reverse=True)
    print(formatted_counts)

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
txt = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
points = re.findall('-?\d+', txt)
points = [int(x) for x in points]
sorted_points = points.sort()
print(f"{abs(points[0] - points[-1])}")

# Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(txt):
    pass

# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
def clean_text(txt):
    matches = re.sub(r'[^A-Za-z0-9 ]', '', txt) # negate of finding all chars
    matches = re.sub(r'[^\w\s]', '', txt) # negate of finding all chars
    return matches
print(clean_text(sentence))
print(most_frequent_words(clean_text(sentence)))