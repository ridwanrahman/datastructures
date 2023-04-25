import numpy as np
# Q: Rotate a N*N matrix by 90 degrees


def missingNumber(myList, totalCount):
    sum1 = (totalCount*(totalCount + 1)/2)
    sum2 = int(sum(myList))
    diff = int(sum1 - sum2)
    print(diff)
    
    return diff


def main():
    myList = [1, 2, 3, 4, 6] 
    total_count = 6
    missingNumber(myList, total_count)
    
if __name__ == "__main__":
    main()