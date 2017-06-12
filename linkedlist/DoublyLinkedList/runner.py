from Node import Node
from doublyLinkedList import DoublyLinkedList

# node1 = Node(1)
# node2 = Node(2)

dl = DoublyLinkedList()
dl.insertAtBeginning(4)
dl.insertAtBeginning(5)
dl.insertAtBeginning(7)
dl.insertAtBeginning(9)
# dl.insertAtPos(10,3)
# dl.insertAtPos(11,0)
# dl.deleteFirstNode()
# dl.deleteLastNode()
# dl.deleteFromPos(2)
dl.deleteFromPos(3)

dl.printList()

