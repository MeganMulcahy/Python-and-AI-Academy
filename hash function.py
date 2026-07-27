# hash function built from scratch. python has built in hash function through the dict. data type

# iterate over text and turn each character into the coresponding unicode using ord() and sum to create the merge of all of them together
def hash_function(text):
    return sum(ord(character) for character in text)

print(hash_function("Lorem"))
print(hash_function("Loren"))
print(hash_function("Loner")) 
# PROBLEM: Can only pass in chars, AND all same letter texts will equate to the same, and letters are sequentail, hash collision
# To solve the issue that we cPassing in key and turning it into a str allows you to pass in any type of value
def hash_function(key):
    return sum(ord(character) for character in str(key))

print(hash_function("Lorem"))
print(hash_function(3.14))
print(hash_function("3.14"))
print(hash_function(True))
# PROBLEM: 3.14 numeric and 3.14 str should ahve different hash codes, but we're treating everything as a str
# To solve this problem we can use repr() which encloses ther representation of strings with additional apostrophes
def hash_function(key):
    return sum(ord(character) for character in repr(key))

print(hash_function(3.14))
print(hash_function("3.14"))

# To solve the anagram issue we can take into account the characters position within the text as well
def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key), start=1)
    )
# multiplying the ordinal values of characters and their indeces
# you enemurate from 1, starting from 0 would discard the first character (value multiplied by 0)
# enumerate takes an iterable and start and adds a counter to each object, returning an enumerate object in 2 forms (index, item)

# PROBLEM: It can grow too large for long input
print(hash_function("This is very long") * 1_000_000)

# PROBLEM: repr() adds two apostrophes so all keys result in an even hash number, causing an uneven distribution of keys
print(hash_function("a"), hash_function("b"), hash_function("c"))

# Solution well remove the left apostrophe if it exists
def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip("'"), start=1)
    )

print(hash_function("a"), hash_function("b"), hash_function("c"))
