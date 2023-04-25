import numpy as np

# Q: Find the max product of two integers in array

def max_of_two_ints(arr):
    res = 0
    indexes = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            mul = arr[i] * arr[j]
            if mul >= res:
                indexes = (arr[i], arr[j])
                res = mul
    
    print(f"{res} from {indexes}")
            
    
def main():
    arr = np.array([4,67 ,6,7])
    resp = max_of_two_ints(arr)
    if resp is not None:
        print(resp)

if __name__ == "__main__":
    main()
