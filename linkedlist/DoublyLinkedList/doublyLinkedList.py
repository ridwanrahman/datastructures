from Node import Node

class DoublyLinkedList:
    def __init__(self):
        self.length=0
        self.head=None
        self.prev=None
    def insertAtBeginning(self, data):
        newNode = Node(data)
        if (self.head == None):
            self.head = self.tail = newNode
            self.length += 1
        else:
            newNode.setPrev(None)
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            self.head = newNode
            self.length += 1

    def insertAtEnd(self, data):
        currentNode = self.head
        newNode = Node(data)
        if (self.head == None):
            self.head = newNode
            self.tail = self.head
        else:
            while currentNode.getNext()!=None:
                currentNode = currentNode.getNext()
            currentNode.setNext(newNode)
            newNode.setPrev(currentNode)
            newNode.setNext(None)

    def getNode(self, pos):
        currentNode = self.head
        count=0
        while (count<pos):
            currentNode = currentNode.getNext()
            count +=1
        return currentNode

    def insertAtPos(self, data, pos):
        newNode = Node(data)
        if self.head == None or pos == 0:
            self.insertAtBeginning(data)
        else:
            tempNode = self.getNode(pos)
            newNode.setPrev(tempNode.getPrev())
            tempNode.getPrev().setNext(newNode)
            newNode.setNext(tempNode)
            tempNode.setPrev(newNode)
            self.length += 1

    def deleteFirstNode(self):
        currentNode = self.head
        tempNode = self.head = currentNode.getNext()
        tempNode.setPrev(None)
        self.length -= 1

    def deleteLastNode(self):
        if (self.length==0):
            raise ValueError("List is already empty")
        else:
            currentNode = self.head
            while (currentNode.getNext()!=None):
                currentNode = currentNode.getNext()
            tempNode = currentNode.getPrev()
            tempNode.setNext(None)
            self.length -= 1

    def deleteFromPos(self, pos):

        if pos>self.length:
            raise ValueError("too big pos")
        elif pos == 0:
            currentNode = self.head.getNext()
            self.head = currentNode
            currentNode.setPrev(None)
            self.length -= 1
        elif self.length-1 == pos:
            currentNode=self.head
            count=0
            while (count<pos):
                currentNode = currentNode.getNext()
                count+=1
            currentNode.getPrev().setNext(None)
            self.length -= 1
        else:
            currentNode = self.getNode(pos)
            nextNode = currentNode.getNext()
            nextNode.setPrev(currentNode.getPrev())
            prevNode = currentNode.getPrev()
            prevNode.setNext(currentNode.getNext())
            self.length -= 1

    def printList(self):
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.getData())
            currentnode = currentnode.next
        # print (self.length)
        print (nodeList)