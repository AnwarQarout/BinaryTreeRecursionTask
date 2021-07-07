class BinTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value > self.value:
            if self.right is None:
                self.right = BinTreeNode(value)
            else:
                self.right.insert(value)

        elif value < self.value:
            if self.left is None:
                self.left = BinTreeNode(value)
            else:
                self.left.insert(value)

    def search(self, value):
        if self is None:
            return None

        elif self.value == value:
            return self

        elif value < self.value:
            return BinTreeNode.search(self.left, value)

        elif value > self.value:
            return BinTreeNode.search(self.right, value)

    def get_tree(self):
        if self.left:
            self.left.get_tree()
        print(self.value),
        if self.right:
            self.right.get_tree()


class BinTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BinTreeNode(value)
        else:
            self.root.insert(value)

    def search(self, value):
        if self.root is None:
            print("Tree is empty")
        else:
            node = self.root.search(value)
            if node is None:
                print("Not found")
            else:
                print("Node found! value = ", node.value)
