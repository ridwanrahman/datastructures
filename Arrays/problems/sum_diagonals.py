# Q: Given 2D list, calculate sum of diagonal elements

def sum_diagonals(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i][i]
    return sum

arr = [[1,2,3], [4,5,6], [7,8,9]]
print(sum_diagonals(arr))