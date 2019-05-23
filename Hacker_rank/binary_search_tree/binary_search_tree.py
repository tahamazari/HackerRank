class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = None

    def insert(self, data):
