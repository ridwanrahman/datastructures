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

    


