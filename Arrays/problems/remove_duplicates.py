# Q: Remove duplicates

def remove_duplicate(arr):
    new_list=[]
 
    for i in arr:
 
        if i not in new_list:
 
            new_list.append(i)
 
    return new_list

def main():
    list1 = [1, 1, 2, 2, 3, 4, 5]
    resp = remove_duplicate(list1)
    print(resp)
    
if __name__ == "__main__":
    main()
    