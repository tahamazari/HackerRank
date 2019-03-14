class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        else:
            print("Traversal type doesn't exist")
            return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.postorder_print(start.right, traversal)
            traversal = self.postorder_print(start.left, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

tree = BinaryTree("B")
tree.root.left = Node("N")
tree.root.right = Node("A")
tree.root.left.left = Node("O")
tree.root.left.left.left = Node("G")
tree.root.left.left.right = Node("U")
tree.root.left.left.left.left = Node("J")


print(tree.print_tree("inorder"))

#                    1
#                 /     \
#                2       3
#              /  \    /   \
#             4    5   6    7
#                            \
#                             8
