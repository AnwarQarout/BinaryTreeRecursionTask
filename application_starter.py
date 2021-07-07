from tree_classes import *

tree = BinTree()
tree.insert(3)
tree.insert(4)
tree.insert(7)
tree.insert(15)
tree.insert(2)

tree.search(7)

tree.root.get_tree()
print("------")
tree.insert(7)
tree.root.get_tree()


