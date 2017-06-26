class BinaryTreeNode:
    # constructor
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data

    def getLeft(self):
        return self.left
    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right
    def setRight(self, right):
        self.right = right
