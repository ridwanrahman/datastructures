# Q: Write a function to find all pairs of an integer array 
# whose sum is equal to a given number. Do not consider commutative pairs.

def pair_sum(array, res):
    final_result = []
    arr = array
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == res:
               final_result.append(f"{str(arr[i])} + {str(arr[j])}")
    print(final_result)

def main():
    list1 = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
    res = 7
    resp = pair_sum(list1, res)
    print(resp)
    
if __name__ == "__main__":
    main()
    