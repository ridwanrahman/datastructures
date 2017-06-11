class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None

    def addNode(self, node):
        self.addBeg(node)

    def addBeg(self, node):
        newNode = node
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def addEnd(self, node):
        newNode = node
        currentNode = self.head
        while currentNode.get_next() != None:
            currentNode = currentNode.get_next()
        currentNode.set_next(newNode)

    def insertAtPos(self, pos, node):
        print (pos)
        newNode = node
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.addBeg(node)
            else:
                current = self.head
                count = 0
                while count < pos - 1:
                    count += 1
                    current = current.get_next()
                newNode.set_next(current.get_next())
                current.set_next(newNode)
                self.length += 1

    def deleteFromBeginning(self):
        if self.length == 0:
            print ("The list is already empty")
        else:
            self.head = self.head.get_next()
            self.length -= 1

    def deleteLastNode(self):
        if self.length==0:
            print ("the list is empty")
        else:
            currentNode = self.head
            previousNode = self.head
            while currentNode.get_next() != None:
                previousNode = currentNode
                currentNode = currentNode.get_next()
            previousNode.set_next(None)
            self.length -= 1
    def deleteFromLinkedListWithNode(self, node):
        if self.length == 0:
            raise ValueError("List is empty")
        else:
            current = self.head
            previous = None
            found = False
            while not found:
                if current == node:
                    print ("found")
                    found = True
                elif current is None:
                    raise ValueError("Node not in linked list")
                else:
                    previous = current
                    current = current.get_next()

            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
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

