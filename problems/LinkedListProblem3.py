#reverse a singly linked list

from singlylinkedlist.linkedlist import LinkedList

ll = LinkedList()
ll.insertSorted(1)
ll.insertSorted(4)
ll.insertSorted(5)
ll.insertSorted(6)
ll.insertSorted(2)
ll.reverseList()
ll.print_list()
