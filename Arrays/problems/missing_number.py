# How to find a missing number in integer array between 1 to 100

def find_missing(arr, n):
    n = (n*(n+1))/2
    sum_list = sum(arr)
    return n - sum_list

def main():
    arr = []
    n = 100
    for i in range(1, 101):
        arr.append(i)
    
    # Removing an item which the find_missing function should find
    arr.remove(43)

    missing = find_missing(arr, n)
    print(missing)


if __name__ == "__main__":
    main()
