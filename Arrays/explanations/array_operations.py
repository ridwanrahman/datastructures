# 1. create an array and traverse
# 2. access individual elements through indexes
# 3. use append() method to append item
# 4. use insert() method
# 5. use extend() method
# 6. add items from list to array using fromlist() method
# 7. remove items using remove() method
# 8. use pop() method
# 9. use index() method
# 10. user reverse() method
# 11. get buffer info using bugger_info() method
# 12. 
# 13.
# 14.
# 15.
# 16.
data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v < element: v = element
 
    return v
print(fun(data[0]))


