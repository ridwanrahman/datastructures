from Node import BinaryTreeNode
from queue import Queue

class BinaryTree:
    def __init__(self):
        self.length=0
        self.size = 0
        self.root = None

    def insertRoot(self, data):
        newNode = BinaryTreeNode(data)
        if self.length == 0:
            self.root = newNode
            self.length += 1
            print (self.root.getRight())
        else:
            print ("root already set")

    def insertLeft(self, data):
        newNode = BinaryTreeNode(data)
        if self.left == None:
            self.left = newNode
            self.length +=1
        else:
            temp = newNode
            temp.left = self.left
            self.left = temp

    def insertRight(self, data):
        newNode = BinaryTreeNode(data)
        if self.right == None:
            self.right = newNode
            self.length +=1
        else:
            temp = newNode
            temp.right = self.right
            self.right = temp

    # def insertInBinaryTreeUsingLevelOrder(self, data):
    #     newNode = BinaryTreeNode(data)
    #     if self.root == None:
    #         print ("there was no root")
    #         self.root = newNode
    #         self.length+=1
    #     else:
    #         root = self.root
    #         q = Queue()
    #         q.enQueue(root)
    #         node = None
    #         while not q.isEmpty():
    #             node = q.deQueue()
    #             if node.getLeft() == None:
    #                 node.setLeft(newNode)
    #                 self.length += 1
    #             else:
    #                 q.enQueue(node.getLeft())
    #             if node.getRight() == None:
    #                 node.setRight(newNode)
    #                 self.length+=1
    #             else:
    #                 q.enQueue(node.getRight())
    def insertInBinaryTreeUsingLevelOrder(root, data):
        newNode = BinaryTree(data)
        if root is None:
            root = newNode
            return root
        q = Queue()
        q.enQueue(root)
        node = None
        while not q.isEmpty():
            node = q.deQueue()
            if data == node.getData():
                return root
            if node.left is not None:
                q.enQueue(node.left)
            else:
                node.left = newNode
                return root
            if node.right is not None:
                q.enQueue(node.right)
            else:
                node.right = newNode
                return root
