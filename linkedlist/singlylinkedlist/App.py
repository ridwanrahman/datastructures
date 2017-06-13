from node import Node
from linkedlist import LinkedList


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
ll = LinkedList()
ll.addNode(node1)
ll.addNode(node2)
ll.addNode(node3)
ll.addNode(node4)
ll.addNode(node5)
# ll.insertAtPos(2, node5)
# ll.deleteFromBeginning()
# ll.deleteLastNode()
# print (ll.listLenght())
ll.deleteFromLinkedListWithNode(node5)
ll.print_list()


        


