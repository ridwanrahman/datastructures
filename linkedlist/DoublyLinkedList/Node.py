class Node:
    # if the data is not given by the user its taken as None
    def __init__(self,data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    #method for setting the data field of the node
    def setData(self, data):
        self.data = data
    #method for getting the data of the node
    def getData(self):
        return self.data
    #method for setting the next location of the node
    def setNext(self, next):
        self.next = next
    #method for getting the next location of the node
    def getNext(self):
        return self.next
    #method that returns True if next node exists
    def hasNext(self):
        return self.next != None
    #method for setting the previous location of a node
    def setPrev(self, prev):
        self.prev = prev
    #method for getting the previous node
    def getPrev(self):
        return self.prev
    #method that returns True if the previous location exists
    def hasPrev(self):
        return self.prev != None
    #method for returning the data of a node as a string 
    def __str__(self):
        return ("Node(Data = %s)")%(self.data)
