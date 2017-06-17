from Node import Node

class CircularLinkedList:
    def __init__(self):
        self.length=0
        self.data = None
        self.next = None
    def circularListLength(self):
        if self.length==0:
            raise ValueError("List is empty")
        currentNode = self.head
        if currentNode == None:
            return 0
        count = 1
        currentNode = currentNode.getNext()
        while currentNode != self.head:
            currentNode = currentNode.getNext()
            count += 1
        return count

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.length==0:
            self.head = newNode
            newNode.setNext(self.head)
            self.length += 1
        else:
            currentNode = self.head
            newNode.setNext(self.head)
            while currentNode.getNext()!=self.head:
                currentNode = currentNode.getNext()
            currentNode.setNext(newNode)
            self.length+=1

    def insertAtFront(self,data):
        if self.length==0:
            newNode = Node()
            newNode.setData(data)
            self.head = newNode
            newNode.setNext(self.head)
            self.length += 1
        else:
            newNode = Node()
            newNode.setData(data)
            newNode.setNext(newNode)
            tempNode = self.head
            while tempNode.getNext() != self.head:
                tempNode = tempNode.getNext()
            tempNode.setNext(newNode)
            newNode.setNext(self.head)
            self.head = newNode
            self.length+=1

    def printList(self):
        nodeList = []
        currentNode =self.head
        nodeList.append(currentNode.getData())
        currentNode = currentNode.getNext()
        while currentNode != self.head:
            nodeList.append(currentNode.getData())
            currentNode = currentNode.getNext()
        print (nodeList)





