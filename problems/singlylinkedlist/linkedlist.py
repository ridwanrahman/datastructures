from .node import Node
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
            newNode.setNext(self.head)
            self.head = newNode
            self.length+=1
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

    def return_list(self):
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append(currentnode.data)
            currentnode = currentnode.next
        return nodeList

    def listLenght(self):
        currentNode = self.head
        count = 1
        while currentNode.get_next()!=None:
            count = count+1
            currentNode = currentNode.get_next()
        return count
    def problem1(self, number):
        count=0
        currentNode=self.head
        found=False
        while not found:
            if (count==number):
                print ("found")
                print (currentNode.getData())
                found=True
            else:
                currentNode = currentNode.getNext()
                count+=1
    def insertSorted(self, number):
        stop=False
        count=0
        previous = None
        if self.head == None:
            self.insertAtBeginning(number)
        else:
            currentNode=self.head
            while currentNode!=None and not stop:
                if currentNode.getData() > number:
                    stop=True
                else:
                    previous=currentNode
                    currentNode = currentNode.getNext()

            temp = Node(number)
            if previous==None:
                temp.setNext(self.head)
                self.head=temp
            else:
                temp.setNext(currentNode)
                previous.setNext(temp)
#Initialize a Node
#check to see if head exists if it doesnt, set that up as the head
#if head doses exist, then get the head Node
#check first node to see if new number is large or not
#if large, set it up as head
#otherwise, go to second Node
#if second node doesnt exist, set it up as second node
#in second node check again if new number is large or not
#if not large, set it there
    def reverseList(self):
        currentNode = self.head
        last=None
        while currentNode!=None:
            nextNode = currentNode.getNext()
            currentNode.setNext(last)
            last=currentNode
            currentNode = nextNode
        self.head=last
    def pop(self):
        currentNode =self.head
        temp = currentNode
        currentNode = currentNode.getNext()
        self.head=currentNode

        return temp.getData()
