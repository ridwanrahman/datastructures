class Node:
    # if the data is not given by the user its taken as None
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None
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