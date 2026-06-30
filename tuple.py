#tuples are unchangeable, ordered and allow duplicates

# syntax
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()

tpl = ('item1', 'item2','item3')
fruits = ('banana', 'orange', 'mango', 'lemon')

len(tpl)
print(len(tpl)) # 3

print(tpl[0]) # item1
print(tpl[1]) # item2
print(tpl[2]) # item3
print(tpl[-1]) # item3
print(tpl[-2]) # item2
print(tpl[-3]) # item1
print(tpl[0:2]) # ['item1', 'item2']
print(tpl[1:]) # ['item2', 'item3']
print(tpl[:2]) # ['item1', 'item2']
print(tpl[:]) # ['item1', 'item2', 'item3']
print(tpl[-2:]) # ['item2', 'item3']
print(tpl[-3:-1]) # ['item1', 'item2']
print(tpl[-3:]) # ['item1', 'item2', 'item3']
print(tpl[::-1]) # ['item3', 'item2', 'item1']
print('item1' in tpl) # True

lst = list(tpl)
print(lst) # ['item1', 'item2', 'item3']

'item2' in tpl # True
print('item2' in tpl) # True   
print('apple' in fruits) # False

tpl2 = ('item4', 'item5','item6')
tpl3 = tpl + tpl2
print(tpl3) # ('item1', 'item2', 'item3', 'item4', 'item5', 'item6')
del tpl

tpl2 += ('item7',) 
# tpl2.append('item7') #AttributeError: 'tuple' object has no attribute 'append'
print(tpl2)

index = len(tpl2) // 2
newitem = 3
tpl2 = tpl2[:index] + (newitem,) + tpl2[index:] # splice up until index (half), then insert, then inclusive from the middle index after
print(tpl2) # ('item4', 'item5', '3', 'item6', 'item7')