class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None
         # method for setting the data field of the node
    def set_data(self, data):
        self.data = data
    # method for getting the data field of the node
    def get_data(self):
        return self.data
      # method for setting the next field of the node
    def set_next(self, next):
        self.next = next
       # method for getting the next field of the node
    def get_next(self):
        return self.next
    # returns true if the node points to another node
    def has_next(self):
            return self.next != None