# A dict is a collection which is unordered, changeable and indexed

# To create a dictionary
my_dict = dict()
my_dict = {
    "one": "un",
    "two": "dos"
}

# To access something in dict is O(1) time complexity.

# dicts are indexed by keys and they can be seen as associative arrays

# Python dicts are implemented using hash tables. Its an array whose indexes are
# obtained using a hash function on the keys. 

# A hash-table is a way of doing key-value lookups. You store the values in an aray,
# then use a hash function to find the index of the array cell that 
# corresponds to your key-value pair.
# a collision is when different keys might have the same hash value. In which case
# they are stored in the same place using linkedlist.

# traversing a dict
my_dict = {"one": "uno", "two": "dos"}

def traverse_dict(dict):
    for key in my_dict:
        print(key, my_dict[key])

traverse_dict(my_dict)

# Searching a dict
def search_dict(dict, value):
    for key in my_dict:
        if my_dict[key] == value:
            return key, value
    return "The value does not exist"

search_dict(my_dict, "uno")

# Deleting an item from dict
# deleting items from dict is O(1) time complexity usually but 
# O(n) in amortized worst case
my_dict = {"one": "uno", "two": "dos"}

my_dict.pop('one')

# removes a random element
my_dict.popitem()

my_dict.clear()

del my_dict['one']

del my_dict

# Dictionary methods
my_dict = {"one": "uno", "two": "dos"}

# this provides a shallow copy of the dict, it does not modify the 
# original dict, but it creates a new dict which is filled with copy of
# references from original dict
new_dict = my_dict.copy()

# fromkeys method creates a new dictionary from the given sequence of elements
# with value provided by user. 
new_dict = {}.fromkeys([1,2,3], [5,6])
print(new_dict)
