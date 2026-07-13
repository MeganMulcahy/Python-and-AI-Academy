# reverse a string
s = "hello"
s = s[::-1]
print(s)

# reverse a string list comprehension
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
print(max(1,2,3,4,5))

# count vowels
s = "Hello"
vowels = "aeiou"
count = sum(1 for char in s.lower() if char in vowels)
print(count)

# union of two sets
set1 = {1,2,3}
set2 = {3,4,5}
result = set1.union(set2)
print(result)

# intersection of two sets
result = set1.intersection(set2)
print(result)

# intersection of two lists
list1= [1,2,3]
list2 = [3,4,5]
intersection = list(set(list1) & set(list2))
print(intersection)

# difference of two sets
result = set1.difference(set2)
print(result)

# difference of lists
difference = list(set(list1) - set(list2))
print(difference)

# add element to set
set1.add(5)

# remove element from set
set1.remove(2)

# factorial of a number
def factorial(n):
    return 1 if n == 0 else n + factorial(n-1)
n = 5
print(factorial(n))

# fibinacci series
def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        print(a, end = "")
        a,b=b,a+b
    print()
fibonacci(7)

# prime number?
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True
print(is_prime(7))

# even or odd
n = 10
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# sum of digits
n = 12345
digit_sum = sum(int(d) for d in str(n))
print(digit_sum)

# remove duplicates from a list
nums = [1,2,2,3,4,4,5]
unique_nums = list(set(nums))
print(unique_nums)

# find second largest element
nums = [10,5,20,8,20,15]
nums = list(set(nums))
nums.sort(reverse = True)
print(nums[1])

# find max and min of a list
nums = [4,7,6,1,9,5]
minimum = min(nums)
maximum = max(nums)
print(minimum, maximum)

# revevrse a list
nums = [1,2,3,4,5]
reversed_nums = nums[::-1]
print(reversed_nums)

# merge two lists
list1 = [1,2,3,4]
list2 = [4,5,6]
merged = list1+list2
print(merged)

# sort a list
nums = [5,2,9,1,5,6]
print(sorted(nums))
nums.sort()
print(nums)

# find common elements
list1 = [1,2,3,4,5]
list2 = [4,5,6,7]
common = list(set(list1) & set(list2))
print(common)
common = set(list1).intersection(list2)
print(common)

# rotate a list
nums = [1,2,3,4,5]
k = 2
k = k % len(nums)
rotated = nums[k:] + nums[:k]
print(rotated)
rotated = nums[-k:] + nums[:-k]
print(rotated)

# list comprehension, create a new list using math inside list
nums = [1,2,3,4,5]
squares = [x**2 for x in nums]
print(squares)

# flatted a nested list
nested = [[1,2], [3,4], [5,6]]
flattened = [item for sublist in nested for item in sublist]
print(flattened)

# count chars including and exluding space
s = "hello world"
count = len(s)
print(count)

# count words
s = "Python is awesome"
words = s.split()
print(len(words))

# count frequ of chars
s = "programming"
freq = {}
for char in s:
    freq[char] = freq.get(char, 0) + 1
print(freq)

# remove spaces
s = "     hello   world   "
result = s.replace(" ", "")
print(result)

# find duplicate chars
s = "programming"
duplicates = set()
for char in s:
    if s.count(char) > 1:
        duplicates.add(char)
print(duplicates)

# first non-repeating char
s = "swiss"
for char in s:
    if s.count(char) == 1:
        print(char)
        break

# check anagram
s1 = "listen"
s2 = "silent"
result = sorted(s1) == sorted(s2)
print(result)

# capitalize words
s = "python is fun"
result = s.title()
print(result)

# reverse words in. a string
s = "Python is awesome"
result = ' '.join(s.split()[::-1])
print(result)

# find longest word
s = "Python is awesome"
words = s.split()
longest = max(words, key = len)
print(longest)

# find word containing the most letter 'e'
s = "Python is awesome weeee"
words = s.split() # whiteout this it results in only a letter
most_e = max(words, key=lambda s: s.count('e'))
print(most_e)

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
data = {'a': 1, 'b': 2, 'c': 3}
data.pop('b')
print(data)

# check if key exists
data = {'a': 1, 'b': 2, 'c': 3}
key = 'b'
exists = key in data
print(exists)

# get all keys
data = {'a': 1, 'b': 2, 'c': 3}
keys = list(data.keys())
print(keys)

# get all values
data = {'a': 1, 'b': 2, 'c': 3}
values = list(data.values())
print(values)

# invert a dictionary (flip keys and values)
data = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in data.items()}
print(inverted)

# sort dict by value
data = {'a': 1, 'b': 2, 'c': 3}
sorted_data = dict(sorted(data.items(), key = lambda x: x[1]))
print(sorted_data)