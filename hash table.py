# hash table
from typing import NamedTuple, Any
from collections import deque

BLANK = object()
DELETED = object()

class Person:
    def __init__(self, name, date_of_birth, married):
        self.name = name
        self.date_of_birth = date_of_birth
        self.married = married

    def __hash__(self):
        return hash(self._fields)

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return self._fields == other._fields

    @property
    def _fields(self):
        return self.name, self.date_of_birth, self.married

class Pair(NamedTuple):
    key: Any
    value: Any

class HashTable:
    def __init__(self, capacity=8, load_factor_threshold=0.6):
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        if not (0 < load_factor_threshold <= 1):
            raise ValueError("Load factor must be a number between (0, 1]")
        self._keys = []
        self._buckets = [deque() for _ in range(capacity)]
        self._load_factor_threshold = load_factor_threshold

    def __len__(self):
        return len(self.pairs)

    def __setitem__(self, key, value):
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()

        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                bucket[index] = Pair(key, value)
                break
        else:
            bucket.append(Pair(key, value))
            self._keys.append(key)

    def _resize_and_rehash(self):
        copy = HashTable(capacity=self.capacity * 2)
        for key, value in self.pairs:
            copy[key] = value
        self._buckets = copy._buckets

    def __getitem__(self, key):
        bucket = self._buckets[self._index(key)]
        for pair in bucket:
            if pair.key == key:
                return pair.value
        raise KeyError(key)

    def __delitem__(self, key):
        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                del bucket[index]
                self._keys.remove(key)
                break
        else:
            raise KeyError(key)

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    @property
    def load_factor(self):
        return len(self) / self.capacity
    
    @property
    def keys(self):
        return self._keys.copy()

    @property
    def values(self):
        return [self[key] for key in self.keys]

    @property
    def pairs(self):
        return [(key, self[key]) for key in self.keys]

    @property
    def capacity(self):
        return len(self._buckets)

    def _index(self, key):
        return hash(key) % self.capacity
    
    def __iter__(self):
        yield from self.keys

    def __str__(self):
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"
    
    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"
    
    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary))
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return set(self.pairs) == set(other.pairs)

    def copy(self):
        return HashTable.from_dict(dict(self.pairs), self.capacity)

    def _probe(self, key):
        index = self._index(key)
        for _ in range(self.capacity):
            yield index, self._slots[index]
            index = (index + 1) % self.capacity

    def _probe(self, key):
        index = self._index(key)
        for _ in range(self.capacity):
            yield index, self._slots[index]
            index = (index + 1) % self.capacity
# tests hashtable

# --- TERMINAL EXECUTION LOGIC ---

def inspect_table_internals(label, ht: HashTable):
    """Prints a full breakdown of the active memory inside the table buckets."""
    print(f"\n=======================================================")
    print(f"📊 INTERNAL STATE: {label.upper()}")
    print(f"=======================================================")
    print(f"• Active Items (Count): {len(ht)}")
    print(f"• Array Capacity:       {ht.capacity}")
    print(f"• Load Factor:          {ht.load_factor:.2f} (Threshold: {ht._load_factor_threshold})")
    print(f"• Tracking Keys Order:  {ht.keys}")
    print(f"\n--- Bucket Distribution Visualization ---")
    
    collision_count = 0
    empty_buckets = 0
    
    for idx in range(ht.capacity):
        bucket = ht._buckets[idx]
        if not bucket:
            empty_buckets += 1
            print(f"  Bucket [{idx:02d}] ── Empty")
        else:
            if len(bucket) > 1:
                collision_count += (len(bucket) - 1)
            
            # Format the deque chain items clearly
            chain_str = " -> ".join([f"({pair.key!r} : {pair.value!r})" for pair in bucket])
            print(f"  Bucket [{idx:02d}] ── [{len(bucket)} item(s)] ──▶ {chain_str}")
            
    print(f"\n📈 Summary Stats: {empty_buckets} empty slots | {collision_count} unresolved hash collisions tracked.")
    print(f"=======================================================\n")


print("--- STARTING DEEP INTERNAL INSPECTION PRINT LOGS ---")

# Step 1: Initializing small to trigger index distributions clearly
demo_table = HashTable(capacity=4, load_factor_threshold=0.75)
inspect_table_internals("Fresh Table (Capacity 4)", demo_table)

# Step 2: Track standard inserts
print("...Inserting item values...")
demo_table["apple"] = 10
demo_table["banana"] = 20
demo_table["cherry"] = 30
inspect_table_internals("After Adding 3 Items", demo_table)

# Step 3: Triggering a replacement update
print("...Overwriting value for 'apple'...")
demo_table["apple"] = 999
inspect_table_internals("After Overwriting 'apple'", demo_table)

# Step 4: Tracking how a Person Object works as a complex key
print("...Creating Custom Objects to watch matching hashes...")
person_a = Person("Alice", "1995-12-17", False)
person_b = Person("Bob", "1988-04-03", True)

demo_table[person_a] = "Developer"
demo_table[person_b] = "Manager"
inspect_table_internals("With Custom Key Objects Added", demo_table)

# Step 5: Watch the items re-balance index footprints after deleting an element
print("...Deleting key 'banana'...")
del demo_table["banana"]
inspect_table_internals("After Deleting 'banana'", demo_table)

# Step 6: Flood keys to show the threshold resize expansion behavior
print("...Flooding entries to force resize_and_rehash expansion threshold...")
for i in range(10):
    demo_table[f"extra_key_{i}"] = i * 100

inspect_table_internals("After Triggering Automatic Resize/Rehash", demo_table)