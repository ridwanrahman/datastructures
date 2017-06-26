class Queue:
    def __init__(self):
        self.queue = []
        self.limit = 10
        self.front = None
        self.rear = None
        self.size = 0
# isEmpty, enQueue, deQueue, queueFront, size, print
    def isEmpty(self):
        return self.size <= 0

    def enQueue(self, data):
        if self.size >= self.limit:
            print ("going beyond limit")
            return
        else:
            self.queue.append(data)
        if self.front is None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1

    def deQueue(self):
        if self.size <= 0 :
            print ("underflow")
            return 0
        else:
            result = self.queue.pop(0)
            self.size -= 1
            if self.size ==0 :
                self.front = self.rear =None
            else:
                self.rear = self.size-1
            return result
    def printRear(self):
        if self.size == 0:
            print ("queueu is empty")
            return 0
        else:
            print (self.queue[self.rear])

    def printFront(self):
        if self.front is None:
            print ("list is empty")
            return 0
        else:
            print (self.queue[self.front])

    def printList(self):
        print (self.queue)
