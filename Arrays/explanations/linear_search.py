import array

array1 = array.array('i', [1, 2, 3, 4])

def linear_search(arr, target):
    for item in arr:
        if item == target:
            return arr.index(item)
        return -1
        
def linear_search_2(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
        return -1
        
# print(linear_search(array1, 4))
print(linear_search_2(array1, 4))