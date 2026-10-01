'''
For 'real' copies we can use the copy module. However, for compound/nested objects (e.g. nested lists or dicts) and custom objects there is an important difference between shallow and deep copying: - shallow copies: Only one level deep. It creates a new collection object and populates it with references to the nested objects. This means modyfing a nested object in the copy deeper than one level affects the original. - deep copies: A full independent clone. It creates a new collection object and then recursively populates it with copies of the nested objects found in the original.
'''


list_a = [1,2,3,4,5]
list_b = list_a

list_a[0] = -10
print(list_a)
print(list_b)

'''
Shallow copy¶
One level deep. Modifying on level 1 does not affect the other list. Use copy.copy(), or object-specific copy functions/copy constructors.
'''
import copy
list_a = [1,2,3,4,5]
list_b = copy.copy(list_a)

# not affects the other list

list_b[0] = -10
print(list_b)
print(list_a)

'''
Shallow copy¶
One level deep. Modifying on level 1 does not affect the other list. Use copy.copy(), or object-specific copy functions/copy constructors.
'''
list_a = [[1,2,3,4,5], [6,7,8,9,10]]
list_b = copy.copy(list_a)

# affects the other

list_a[0][0] = -10
print(list_a)
print(list_b)

# we can also use the following to create shallow copies:

# shallow copies
list_b = list(list_a)
list_b = list_a[:]
list_b = list_a.copy()