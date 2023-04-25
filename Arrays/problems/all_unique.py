# Write a program to check if an array contains all unique numbers

def is_array_unique(arr):
    a = []
    for i in range(len(arr)):
        if arr[i] in a:
            return False
        else:
            a.append(arr[i])
    
    return True

def main():
    arr = [1,2,3,1]
    resp = is_array_unique(arr)
    print(resp)
    

if __name__ == "__main__":
    main()
