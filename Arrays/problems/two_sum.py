# Write a program to find all pairs of integers 
# whose sum is equal to a given number

# For this question, we are writing a function that takes in the 
# array and the target that we have to add it upto. Then, we are running
# a for loop from the start to the end of the array. Inside that loop
# we are running a second loop that picks up that item and runs from its
# next to the end. for each, we are checking whether they add upto the target
# if it does, we are appending the indexes into another list and finally
# once the loops end, we are returning it back.

def two_sum(arr, n):
    final_sol = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                continue
            addition = arr[i] + arr[j]
            if addition == n:
                final_sol.append((i, j))
    
    return final_sol

def main():
    arr = [1,2,3,2,3,4,5,6]
    n = 6
    resp = two_sum(arr, n)
    print(resp)
    

if __name__ == "__main__":
    main()
    
    
