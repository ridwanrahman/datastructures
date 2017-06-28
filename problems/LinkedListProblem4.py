# Palindrome checking

from singlylinkedlist.linkedlist import LinkedList

print ("enter a word")
word_input=input()
ll=LinkedList()
word_input_array=[]
for i in word_input:
    ll.insertAtEnd(i)
    word_input_array.append(i)
ll.reverseList()
stop=False
i=len(word_input)-1
count=0
palindrome=False
while count<=i and not stop:
    reverse_pop = ll.pop()
    if word_input_array[count] == reverse_pop:
        count+=1
        palindrome=True
    else:
        print ("not palindrome")
        palindrome=False
        stop=True
if palindrome:
    print ("palindrome")
