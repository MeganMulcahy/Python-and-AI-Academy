st = set()
st = {1, 2, 3, 4, 5}
len(st)

#contain item
print('Does set st contain objet 3?', 3 in st)

#sets are unordered and all unique elements

#adding an item to a set
st.add(6)
st.add('item7')
print(st)

#update/add multiple items to a set
#adding a duplicate item will have no effect and not raise an error
st.update([8, 7, 9])
st.add(6)
print(st)

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits)

#remove() method. If the item is not found remove() method will raise errors
#so check if it exists before removing it
st.remove('item7')
if 'item7' in st:
    st.remove('item7')

st.discard('item7') #discard() method will not raise an error if the item is not found
st.discard(6)
print(st)

#The pop() methods remove a random item from a list and it returns the removed item.
print(fruits)
removed_item = fruits.pop()
print(fruits)
print(removed_item)

#clear() method empties the set
fruits.clear()
print(fruits)

del st

#converting list to set
list = [1, 2, 3, 4, 1]
st = set(list)
print(st)

#converting string to set
str = 'hello world'
ststr = set(str)
print(ststr)

#converting tuple to set
#tuple is orders, unchangable and allows duplicats
#set is unordered, changable but not editable and does not allow duplicates
tup = (1, 2, 3, 4, 5)
sttup = set(tup)
print(sttup)

#joining sets
st1 = {1, 2, 3}
st2 = {3, 4, 5}
st3 = st1.union(st2)
print(st3)
st1.update(st2)
print(st1)

#intersect
st1 = {1, 2, 3}
st2 = {3, 4, 5}
intersect = st1.intersection(st2)
print(intersect)

python = set("python")
dragon = set("dragon")
on = set("on")
python.intersection_update(dragon)
print(python)

#subset and superset
#superset is a collection that contains all elements of another smaller collection
print(on.issubset(python))
print(python.issuperset(on))


#difference
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1)) # set() : st2 - st1
print(st1.difference(st2)) # {'item1', 'item4'} => st1\st2  : st1 - st2

#symmetric difference / all items - the items that are in both
st1 = {1, 2, 3, 4}
st2 = {3, 4}
print(st1.symmetric_difference(st2)) # {1, 2} => st1^st2 : st1 - st2 + st2 - st1

#disjoint sets/doesnt overlap at all
st1 = {1, 2, 3}
st2 = {4, 5}
print(st1.isdisjoint(st2)) # True
print(st2.isdisjoint(st1))
st2 = {3, 4, 5}
print(st1.isdisjoint(st2)) # False
print(st2.isdisjoint(st1)) # False


#comparing list string to set len
age = [22, 19, 24, 25, 26, 24, 25, 24]
set_age = set(age)
print(len(age)) # 8
print(len(set_age)) # 5 bc overlapping values