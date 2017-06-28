#given a linked list with even and odd numbers, create an algorithm for making changes to the list in such a way
#that all even numbers appear at the beginning

from singlylinkedlist.linkedlist import LinkedList

ll = LinkedList()
ll.insertSorted(1)
ll.insertSorted(3)
ll.insertSorted(8)
ll.insertSorted(19)
ll.insertSorted(16)
ll.insertSorted(17)
ll.print_list()
ll_even = LinkedList()
ll_odd = LinkedList()

for i in range(ll.listLenght()):
    popped_num = ll.pop()
    if popped_num%2==0:
        ll_even.insertSorted(popped_num)
    else:
        ll_odd.insertSorted(popped_num)

ll_even.print_list()
ll_odd.print_list()

for i in range(ll_even.listLenght()):
    popped_num = ll_even.pop()
    ll.insertAtEnd(popped_num)
for i in range(ll_odd.listLenght()):
    popped_num = ll_odd.pop()
    ll.insertAtEnd(popped_num)

ll.print_list()
