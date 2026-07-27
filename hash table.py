def hash_function(key):
    return sum(
        index * ord(character)
        for index, character in enumerate(repr(key).lstrip("'"), start=1)
    )

class HashTable:
    def __init__(self, size):
      self.size = size
      self.hash_table = [[] for _ in range(size)] # inits table with empty [] lists each serving as a bucket to hold key–value pairs - enables chaining

    def set_val(self, key, val):
        hashed_key = hash_function(key) % self.size # calculates the bucket inde where the key value pair will be stored
        bucket = self.hash_table[hashed_key] # retrieves the list existing on that index in the hash table

        for index, (recordkey, _) in enumerate(bucket):
            if recordkey == key: # checks if key already exists in bucket, if found update the existing value
                bucket[index] = (key, val)
                return
        bucket.append((key, val)) # if not found, append the new key-value pair

    def get_val(self, key):
        hashed_key = hash_function(key) % self.size
        bucket = self.hash_table[hashed_key]

        # finds the bucket where the key should be
        # searches for key in bucket and returns value or error
        for recordkey, recordval in bucket:
            if recordkey == key:
                return recordval
        return "No record found"

    def delete_val(self, key):
        hashed_key = hash_function(key) % self.size
        bucket = self.hash_table[hashed_key]

        # finds the buckets where the key should be
        # searches for key in bucket and removes the key-value pair or does nothing
        for index, (recordkey, _) in enumerate(bucket):
            if recordkey == key:
                bucket.pop(index)
                return
    # or you can use the built in del function
    # del hashTable[key]
    # def __delitem__(self, key):
    #     self.delete_val(key)
    
    # DISPLAU function (print)
    def __str__(self):
        return "".join(str(bucket) for bucket in self.hash_table)

ht = HashTable(3)
print(ht)

ht.set_val('apple', 10)
ht.set_val('banana', 20)
ht.set_val('cherry', 30)
ht.set_val('peach', 40)

print("Hash Table:", ht)

print("Value for 'banana':", ht.get_val('banana'))
print("Value for 'apple':", ht.get_val('apple'))

ht.set_val('apple', 50)
print("Updated Hash Table:", ht)

ht.delete_val('banana')
print("After Deletion:", ht)

print("Value for 'banana':", ht.get_val('banana'))