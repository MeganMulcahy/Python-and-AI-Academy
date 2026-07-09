# reverse a string
s = "hello"
s = s[::-1]
print(s)

s = "hello"
reversed = ""
for i in s:
    reversed = i + reversed
print(reversed)

# check palindrome
s = "poop"
print(s[::-1] == s)

#check palindrome ignoring spaces etc.
def isPalindrome(s):
        s = "".join(filter(str.isalnum, s.lower()))
        return s[::-1] == s
s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))

# find largest number


# swap two variables


# count vowels


# union of two sets

# intersection of two sets

# difference of two sets

# symmetric difference

# check subset

# check superset

# check disjoint sets

# add element to set

# remove element from set

# factorial of a number

# fibinacci series

# prime number?

# even or odd

# sum of digits

# remove duplicates from a list

# find second largest element

# find max and min

# revevrse a list

# merge two lists

# sort a list

# find common elements

# rotate a list

# list comprehension, create a new list using math inside list

# flatted a nested list

# count chars including and exluding space

# count words

# count frequ of chars

# remove spaces

# find duplicate chars

# first non-repeating char

# check anagram

# capitalize words

# reverse words in. a string

# find longest word

# count frequency of elements
nums = [1,2,2,3,3,3,4,4,4,4]
freq = {} #Create a dict map
for num in nums:
    freq[num] = freq.get(num, 0) + 1
print(freq)

# merge two dicts
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = {**dict1, **dict2}
print(merged)

# find key with max value
data = {'a': 10, 'b': 25, 'c': 15}
max_key = max(data, key = data.get)
print(max_key, data[max_key])

# remove a key from a dictionary

# check if key exists

# get all keys

# get all values

# invert a dictionary (flip keys and values)

# sort dict by value

# remove duplicates
