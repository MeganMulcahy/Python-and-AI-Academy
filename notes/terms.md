### Number Integer:
- Integer (negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...
- Float: Decimal number Example ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...
- Complex Example 1 + j, 2 + 4j

### String
- A collection of one or more characters under a single or double quote. If a string is more than one sentence then we use a triple quote.

- `isnumeric()`: checks if all characters in a string are numbers or number related (just like `isdigit()`, just accepts more symbols, like ½)
- `isdigit()`: checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
- `isdecimal()`: checks if all characters in a string are decimal (0-9)
- `isalpha()`: checks if all string elements are alphabet characters (a-z and A-Z)
- `isidentifier()`: checks if a string is a valid identifier - a valid variable name
- `islower()`: checks if all alphabet characters in the string are lowercase
- `isupper()`: checks if all alphabet characters in the string are uppercase
- `join(iterable)`: returns a concatenated string, inserting the string as a separator between elements of iterable
- `strip(chars=None)`: removes all given characters (whitespace by default) starting from the beginning and end of the string
- `swapcase()`: converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
- `startswith(prefix)`: checks if the string starts with the specified string
- `title()`: returns a title cased string

### Booleans
- A boolean data type is either a True or False value. T and F should be always uppercase.

### List
- Python list is an ordered collection which allows to store different data type items. Uses `[ ]`.

- Indexing: Exclusive End: The end index is never included, No Errors
    - Positive Indexing (Left-to-Right) Indices: Start at 0 for the first item. Defaults: `start = 0`, `end = len(lst)`, `step = 1`.
        - `lst[1:4]` → Items at index 1, 2, and 3. `lst[:3]` → Items from the beginning up to index 3 (exclusive).
        - `lst[::2]` → Every second item from start to finish.
    - Negative Indexing (Right-to-Left) Indices: The last item is -1, second-to-last is -2. Defaults: Omitted values adapt to match the step direction.
        - `lst[-3:-1]` → Extracts from third-to-last up to (but excluding) the last item.
        - `lst[:-2]` → Extracts everything from the start up to the third-to-last item.
        - `lst[::-1]` → Reverses the entire list.

- `item in list`: "in" operator (not a callable) that checks if an item is a member of a list
- `append(item)`: adds item to the end of an existing list
- `insert(index, item)`: inserts a single item at a specified index in a list. Other items are shifted to the right.
- `remove(item)`: removes the first matching specified item from a list
- `pop(index)`: removes and returns the item at the specified index (or the last item if index is not specified). Unlike `del`, it returns the removed value.
- `del list[index]`: removes the specified index, and can also delete items within an index range or delete the entire list. Does not return anything.
- `clear()`: empties the list, removing all items
- `copy()`: creates and returns a duplicate of the list
- `extend(iterable)`: joins, or concatenates, two lists together (the `+` operator does the same without modifying the original)
- `count(item)`: returns the number of times an item appears in a list
- `index(item)`: returns the index of an item in the list
- `reverse()`: reverses the order of a list in place
- `sort(reverse=False)`: reorders the list items in ascending order and modifies the original list. Pass `reverse=True` to arrange in descending order instead.
- `sorted(iterable)`: returns a new ordered list without modifying the original list

### Dictionary
- A Python dictionary object is an unordered collection of data in a key value pair format.
```
{
    'first name': 'Megan',
    'age': 23,
    'skills': ['Python', 'AI']
}
```
- Keys must be unique and immutable. Uses `{}` with colons separating keys and values.

- `len(dict)`: returns the total number of key: value pairs in the dictionary.
- `get(key, default=None)`: accesses a value safely; returns None or a default value instead of throwing a KeyError if the key is missing.
- `items()`: returns a view object containing the (key, value) pairs as a list of tuples, useful for looping.
- `keys()`: returns a view object of all the keys present in the dictionary.
- `values()`: returns a view object of all the values present in the dictionary.
- `pop(key)`: removes the specified key and returns its corresponding value.
- `popitem()`: removes and returns the last inserted (key, value) pair as a tuple.
- `copy()`: creates and returns a shallow copy of the dictionary.
- `clear()`: removes all elements from the dictionary, leaving it completely empty.
- `del dict[key]`: keyword that completely destroys the specified key (or the whole dictionary variable from memory if used without a key).
- `key in dict`: "in" operator (not a callable) used to check if a specific key (not value) exists within the dictionary.

### Hash Table (dict in Python)
- A **hash** is a mathematical process that takes an input of any size and converts it into a smaller, fixed-size sequence of bytes (called a hash value or hash code). In Python, this is used as a fast indexing system. Instead of searching through data line-by-line, Python converts a key into a hash number to find its exact location in memory instantly.
    - Python dictionaries use this hashing process under the hood to store and look up key-value pairs instantly. Every key must have a value, but they can be any arbitrary data type like numbers or words.
    - You can only hash data types that can never change (immutable). This means strings, numbers, and tuples are allowed, but lists, sets, and dictionaries are forbidden.
    - Hashing is used to secure passwords. While Python uses a global `hash()` function for dictionaries and sets, it includes a built-in `hashlib` module for these cryptographic security functions.
    - **Collision Handling:**
        - Chaining: Store multiple key-value pairs in the same bucket, usually as a list or linked list.
        - Open Addressing / Rehashing: If a collision occurs, find another empty bucket according to some probing method (linear probing, quadratic probing, etc.).
    - Python dictionaries (dict) are implemented as hash maps.
    - You can create a custom hash map (like your HashTable class) to understand how hash maps work internally.

### Tuple
- A tuple is an ordered collection of different data types like list but tuples can not be modified once they are created. They are immutable. Uses `( )`.

- `tuple(iterable)`: creates a tuple (empty if no argument is given)
- `count(item)`: counts the number of times a specified item appears in a tuple
- `index(item)`: finds the index of a specified item in a tuple
- `tuple1 + tuple2`: "+" operator (not a callable) that joins two or more tuples together to create a new tuple
- slicing: same as lists.

- To add an item wherever you want, you can use `+` to add at the end, or slice in the middle where you want it, and `+` both ends:
```python
mytuple = mytuple[:index] + (new_item,) + mytuple[index:]
```
- It's the `(new_item,)` comma that identifies that as a tuple containing 1 item instead of an int.
- We can change tuples to lists and lists to tuples. Tuple is immutable — if we want to modify a tuple we should change it to a list.
- Joining tuples using `+`, no `extend()` because tuples can't be modified.

- `del tuple`: deletes the entire tuple (individual elements cannot be deleted since tuples are immutable)

```python
# Convert the list to a tuple
my_tuple = tuple(my_list)
```

### Set
- A set is a collection of data types similar to list and tuple. Unlike list and tuple, set is not an ordered collection of items. Uses `{ }`.

- `add(item)`: adds a single item to a set; duplicates are ignored without throwing an error
- `update(iterable)`: adds multiple items from an iterable (list, tuple) into a set
- `remove(item)`: deletes a specific item from a set; throws an error if the item is not found
- `discard(item)`: deletes a specific item from a set; does not throw an error if the item is not found
- `pop()`: removes and returns a random item from the set
- `clear()`: empties the set entirely
- `del set`: deletes the set variable completely from memory
- `set(iterable)`: converts a list, string, or tuple into a set of unique elements
- `union(other_set)`: joins sets together, returning a new set with all unique elements from both
- `intersection(other_set)`: returns a new set containing only the items that exist in both sets
- `intersection_update(other_set)`: modifies the original set to keep only the items found in both sets
- `issubset(other_set)`: checks if all elements of the current set belong to another set
- `issuperset(other_set)`: checks if the current set contains all elements of another smaller collection
- `difference(other_set)`: returns a new set with elements in the first set that are not in the second
- `symmetric_difference(other_set)`: returns a new set with all items across both sets, minus the items they share in both
- `isdisjoint(other_set)`: checks if two sets share zero elements, returning True if they do not overlap at all

![alt text](image.png)

### String Formatting
- `%s` - String (or any object with a string representation, like numbers)
- `%d` - Integers
- `%f` - Floating point numbers
- `"%.<number of digits>f"` - Floating point numbers with fixed precision

### For loops
- `break`: keyword (not a callable, no parentheses/args) that stops the loop before it is completed
- `continue`: keyword (not a callable, no parentheses/args) that skips the rest of the current iteration and moves to the next one
- `range(start, stop, step)`: returns a sequence of numbers. Takes three parameters: starting, ending and increment. By default it starts from 0 and the increment is 1. The range sequence needs at least 1 argument (stop). stop is non-inclusive.
- `pass`: keyword (not a callable, no parentheses/args) used on empty for loops (or other empty blocks) to avoid errors

### Built-in Functions & Higher Order Functions (work with any iterable — list, tuple, string, set, dict — not tied to one data type)
- `lambda args: expr`: keyword syntax (not a callable) that creates an inline anonymous function, e.g. used inside `filter()`, `map()`, or `sorted()`. Example: `add_ten = lambda x: x + 10`
- `enumerate(iterable, start=0)`: returns an iterator of (index, item) pairs, useful for looping when you need both the index and the value
- `zip(*iterables)`: combines multiple iterables element-wise into an iterator of tuples, stopping as soon as the shortest iterable is exhausted
- `any(iterable)`: returns True if at least one element in the iterable is truthy (returns False on an empty iterable)
- `all(iterable)`: returns True if every element in the iterable is truthy (returns True on an empty iterable)
- A `higher order function` is a function that accepts another function or returns another function. Built in higher order functions (`map()`, `filter()`, `reduce()`, `sorted()`)
- `Decorator`: A design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.
    - you use decorators for code reusability. write the wrapper logic once and apply it to ten functions using a single line.
    - checks if users logged in before letting the see a profile page `@login_required`
    - can be used to cache results easily and it just kind of adds another funtion to whats already going to run `@lru_cache`
- `Closures`: Python allows a nested function to access the outer scope of the enclosing function. This is is known as a Closure. Let us have a look at how closures work in Python. In Python, closure is created by nesting a function inside another encapsulating function and then returning the inner function. See the example below.
- `filter(function, iterable)`: extracts elements from an iterable based on whether they meet a specific condition. Returns a lazy generator object, not a finished list or string — convert it into a concrete data type using `list()`, `tuple()`, or `"".join()`
    - makes a boolean for each item in iterable and only returns the true
- `map(function, iterable)`: applies a function to every item in an iterable, returning a lazy iterator of the results (like `filter()`, convert it with `list()`, `tuple()`, etc. to see the values)
    - Why it matters: It computes values on demand instead of loading everything into memory at once.
    - Example: If you have 10 million items, map() consumes almost zero memory upfront, whereas a list comprehension will instantly allocate memory for all 10 million elements.
- `reduce(function, iterable)`: Function is defined in the functools module and we should import it from this module. Like `map()` and `filter()` it takes two parameters, a function and an iterable. However, it does not return another iterable, instead it returns a single value.
- `sorted(interable, key)`: key uses lambda function


### Modules
- OS Module: performing operating systme tasks, creating, changing working dir, removing a dir/folder, fetching contents, etc.
- Sys Module: functions and variables to manipluate diff parts of Python runtime env. Function sys.argv returns a list of command line args passed into a Python script. Item at index 0 is always the name of the script, item 1 is the arg passed in from command line.
    - #print(sys.argv[0], argv[1],sys.argv[2])  # this line would print out: filename argument1 argument2
- Statistics: Math stats functions for numerical data. mean, median, mode, stdev, etc.
- Math Module: Mathematic operations and constants. pi, sqrt, power, floor, ceil, log10,etc. To check what functions the module has got, we can use help(math), or dir(math). This will display the available functions in the module. If we want to import only a specific function from the module we import it as follows:
    - from math import pi, sqrt
- String Module: ascii_letters returns alphabeticals, .digits, .punctuation, .hexadecimal, etc.
- Random Module: 
    - `random.random()` gives us a random float between 0-0.9999. 
    - `randint(a, b)` gives us a random integer between a and b inclusive. 
    - `choice(seq)` returns a single random item from a sequence. 
    - `choices(population, k=n)` returns a list of n random items, with replacement (duplicates allowed). 
    - `sample(population, k=n)` returns a list of n unique random items, without replacement (no duplicates).