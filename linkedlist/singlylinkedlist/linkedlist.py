from node import Node
class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode
        self.length += 1

    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head == None:
            raise ValueError("List is empty")
        else:
            currentNode = self.head
            while currentNode.getNext()!=None:
                currentNode = currentNode.getNext()
            currentNode.setNext(newNode)
            self.length+=1


    def insertAtPos(self, pos, data):
        newNode = Node(data)
        if pos > self.length or pos < 0:
            raise ValueError("Problem with entering valeu in the list")
        else:
            if pos == 0:
                self.insertAtBeginning(data)
            else:
                currentNode = self.head
                count = 0
                while count < pos - 1:
                    count += 1
                    currentNode = currentNode.getNext()
                newNode.setNext(currentNode.getNext())
                currentNode.setNext(newNode)
                self.length += 1

    def deleteFromBeginning(self):
        if self.length == 0:
            print ("The list is already empty")
        else:
            self.head = self.head.getNext()
            self.length -= 1

    def deleteLastNode(self):
        if self.length==0:
            print ("the list is empty")
        else:
            currentNode = self.head
            previousNode = self.head
            while currentNode.getNext() != None:
                previousNode = currentNode
                currentNode = currentNode.getNext()
            previousNode.setNext(None)
            self.length -= 1
    def deleteFromLinkedListWithNode(self, data):
        if self.length == 0:
            raise ValueError("List is empty")
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current.getData() == data:
                    print ("found")
                    found = True
                elif current is None:
                    raise ValueError("Node not in linked list")
                else:
                    previous = current
                    current = current.getNext()
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
                self.length -= 1
    def print_list(self):
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.next
        print (nodeList)

    def listLenght(self):
        currentNode = self.head
        count = 1
        while currentNode.get_next()!=None:
            count = count+1
            currentNode = currentNode.get_next()
        return count
