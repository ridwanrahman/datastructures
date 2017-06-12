class Node:
    # if the data is not given by the user its taken as None
    def __init__(self,data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    #method for setting the data field of the node
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self, next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self):
        return self.next != None
    def setPrev(self, prev):
        self.prev = prev
    def getPrev(self):
        return self.prev
    def hasPrev(self):
        return self.prev != None


    def __str__(self):
        return ("Node(Data = %s)")%(self.data)