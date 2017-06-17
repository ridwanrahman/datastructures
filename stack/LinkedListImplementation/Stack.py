from Node import Node

class Stack:
    def __init__(self):
        self.head = None
        self.length = 0
        self.temp_first_node = 0
        self.first_node=None

    def push(self,data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            newNode.setNext(self.head)
            self.head = newNode
            self.temp_first_node = newNode
            self.length += 1
        else:
            newNode.setNext(self.head)
            self.head = newNode
            self.length +=1

    def run(self):
        a = []
        a.append(self.head.getData())
        while self.head != self.temp_first_node:
            self.head = self.head.getNext()
            a.append(self.head.getData())
        print (a)



# push, pop, peek
