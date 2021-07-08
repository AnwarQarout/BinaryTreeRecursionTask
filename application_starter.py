from tree_classes import *

tree = BinTree()
tree.insert(3)
tree.insert(4)
tree.insert(7)
tree.insert(15)
tree.insert(2)
tree.search(15)

list_num = list()
list_num=tree.root.tree_returner_helper()
print(list_num)


