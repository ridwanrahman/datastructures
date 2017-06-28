# Insert a node in a sorted linked list
from singlylinkedlist.linkedlist import LinkedList


ll = LinkedList()
# ll.insertAtBeginning(2)
# ll.insertAtBeginning(3)
# ll.insertAtBeginning(4)
ll.insertSorted(78)
ll.insertSorted(100)
ll.insertSorted(90)
ll.insertSorted(9)
ll.insertSorted(900)
ll.print_list()
