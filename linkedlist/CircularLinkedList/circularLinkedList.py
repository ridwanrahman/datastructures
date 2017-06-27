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
        newNode.setNext(newNode)
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
        newNode = Node()
        newNode.setData(data)
        newNode.setNext(newNode)
        if self.length==0:
            self.head = newNode
            newNode.setNext(self.head)
            self.length += 1
        else:
            tempNode = self.head
            while tempNode.getNext() != self.head:
                tempNode = tempNode.getNext()
            tempNode.setNext(newNode)
            newNode.setNext(self.head)
            self.head = newNode
            self.length+=1

    def insertAtPos(self, pos, data):
        if pos>self.length+1:
            raise ValueError("input number too big")
        newNode = Node()
        newNode.setData(data)
        newNode.setNext(newNode)
        if self.length == 0:
            self.head = newNode
            newNode.setNext(self.head)
            self.length += 1
        else:
            count = 1
            found=False
            currentNode = self.head
            while not found:
                if (pos==1):
                    self.insertAtFront(data)
                    found =True
                elif(pos==self.length+1):
                    self.insertAtEnd(data)
                    found=True
                elif(count == pos-1):
                    newNode.setNext(currentNode.getNext())
                    currentNode.setNext(newNode)
                    self.length+=1
                    found=True
                else:
                    currentNode = currentNode.getNext()
                    count += 1

    def deleteLast(self):
        if self.length==0:
            raise ValueError("List is already empty")
        else:
            temp = self.head
            currentNode = self.head
            if currentNode.getNext() == self.head:
                raise ValueError("list is empty")
            while currentNode.getNext() != self.head:
                temp = currentNode
                currentNode = currentNode.getNext()
            temp.setNext(currentNode.getNext())
            self.length -= 1

    def deleteFirst(self):
        if self.length==0:
            raise ValueError("List is already empty")
        else:
            currentNode =self.head
            nextCurrentNode = currentNode.getNext()
            if currentNode.getNext() == self.head:
                raise ValueError("List is empty")
            while currentNode.getNext() != self.head:
                currentNode = currentNode.getNext()
            currentNode.setNext(nextCurrentNode)
            self.head = nextCurrentNode
            self.length -= 1

    def printList(self):
        nodeList = []
        currentNode =self.head

        nodeList.append(currentNode.getData())
        currentNode = currentNode.getNext()
        while currentNode != self.head:
            nodeList.append(currentNode.getData())
            currentNode = currentNode.getNext()
        print (nodeList)
