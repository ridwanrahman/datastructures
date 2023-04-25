import numpy as np

# Q: How to check if an array contains a number?
# For this question, we can use the in operator, but 
# we are checking manually by creating a numpy array.
def find_in_array(arr, n):
    index = None
    for i in range(len(arr)):
        if arr[i] == n:
            index = i
            break
    if index:
        return index
    return None

def main():
    arr = np.array([4,5,6,7])
    n = 23
    resp = find_in_array(arr, n)
    if resp is not None:
        print(resp)

if __name__ == "__main__":
    main()