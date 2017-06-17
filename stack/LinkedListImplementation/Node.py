class Node:
    def __init__(self):
        self.data = None
        self.next = None
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data
    def getNext(self):
        return self.next
    def setNext(self, next):
        self.next = next
    def hasNext(self):
        return self.next != None
