class Stack:
    def __init__(self):
        self.stack = []
        self.limit = 10
# isEmpty, push, pop, peek, size
    def isEmpty(self):
        return len(self.stack) <= 0

    def push(self, value):
        if len(self.stack) >= self.limit:
            print ("Stack overflow")
        else:
            self.stack.append(value)
    def pop(self):
        if len(self.stack) <= 0:
            print ("stack underflow")
        else:
            self.stack.pop()

    def peek(self):
        if len(self.stack)<=0:
            print ("stack uderflow")
            return 0
        else:
            return self.stack[-1]
    def size(self):
        return len(self.stack)

    def print_stack(self):
        a = []
        for i in self.stack:
            a.append(i)
        print (a)

if __name__ == "__main__":
    app = Stack()
    app.push(1)
    app.push(2)
    app.push(3)
    app.push(4)
    app.push(5)
    app.print_stack()
    app.pop()
    # print (app.size())
