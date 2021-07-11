class BinTreeNode:
    def __init__(self, value):
        if isinstance(value,int):
            self.value = value
            self.left = None
            self.right = None
        else:
            raise TypeError("Entered non integer value.")

    def insert(self, value):
        if not isinstance(value,int):
            raise TypeError("Entered non integer value")
        else:
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
        if not isinstance(value,int):
            raise TypeError("Entered non integer value")
        else:
            if self is None:
                return None

            elif self.value == value:
                return self

            elif value < self.value:
                return BinTreeNode.search(self.left, value)

            elif value > self.value:
                return BinTreeNode.search(self.right, value)


    def tree_returner_helper(self):
        list_nums=list()
        if self is None:
            return []
        else:
            list_nums= self.get_tree(list_nums)
            return list_nums


    def get_tree(self,list_nums):
        if self.left:
            self.left.get_tree(list_nums)
        list_nums.append(self.value)
        if self.right:
            self.right.get_tree(list_nums)
        return list_nums


class BinTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not isinstance(value, int):
            raise TypeError("Entered non integer value")
        else:
            if self.root is None:
                self.root = BinTreeNode(value)
            else:
                self.root.insert(value)

    def search(self, value):
        if not isinstance(value, int):
            raise TypeError("Entered non integer value")
        else:
            if self.root is None:
                print("tree is empty")
                return "tree is empty"
            else:
                node = self.root.search(value)
                if node is None:
                    print("Node not found!")
                    return "Node not found."
                else:
                    print("Node found! value = ", node.value)
                    return "Node found! value =",node.value
