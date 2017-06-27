class Node:
    #constructor
    def __init__(self):
        self.data = None
        self.next = None
    #method for setting the data of the node
    def setData(self, data):
        self.data = data
    #method for getting the data of the node
    def getData(self):
        return self.data
    #method for setting the next location
    def setNext(self, next):
        self.next = next
    #method for getting the next location of the node
    def getNext(self):
        return self.next
    #method that returns True if the next node exists
    def hasNext(self):
        return self.next != None
