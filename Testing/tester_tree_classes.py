import inspect
import unittest


nodes_to_insert = [1,5,2,4,7,8]
error_raise_tests = ["hello","",[],1.4]

from tree_classes import BinTree, BinTreeNode


class BinTreeTester(unittest.TestCase):

    def setUp(self):
        self.logPoint()
        self.tree = BinTree()



    def test_init(self):
        self.logPoint()
        self.assertEqual(self.tree.root,None)



    def test_insert(self):
        self.logPoint()
        for node in nodes_to_insert:
            self.tree.insert(node)
        with self.subTest():
            self.assertNotEqual(self.tree.root,None)
            self.assertEqual(self.tree.root.value,1)
            self.assertEqual(self.tree.root.right.value,5)
            self.assertEqual((self.tree.root.search(5)).left.value,2)
        for error in error_raise_tests:
            with self.subTest():
                self.assertRaises(TypeError,BinTree.insert,BinTree,error,True)




    def test_search(self):
        self.logPoint()
        self.assertEqual(self.tree.search(6),"tree is empty")
        for node in nodes_to_insert:
            self.tree.insert(node)
        self.assertNotEqual(self.tree.search(6),"tree is empty")
        self.assertEqual(self.tree.search(6),"Node not found.")
        self.assertEqual(self.tree.search(5), ('Node found! value =', 5))
        for error in error_raise_tests:
            with self.subTest():
                self.assertRaises(TypeError, BinTree.search, BinTree, error, True)


    def tearDown(self) -> None:
        self.logPoint()



    def logPoint(self):
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))


class BinTreeNodeTester(unittest.TestCase):

    def setUp(self):
        self.logPoint()
        self.node = BinTreeNode(5)


    def test_init(self):
        self.logPoint()
        self.assertEqual(self.node.left,None)
        self.assertEqual(self.node.right, None)
        self.assertEqual(self.node.value, 5)

        for node in error_raise_tests:
            with self.subTest():
                self.assertRaises(TypeError,BinTreeNode,node,True)


    def test_insert(self):
        self.logPoint()
        for node in nodes_to_insert:
            self.node.insert(node)
        with self.subTest():
            self.assertEqual(self.node.right.value,7)
            self.assertEqual(self.node.left.value,1)
            self.assertEqual(self.node.right.right.value,8)
            self.assertEqual(self.node.left.left,None)
        for error in error_raise_tests:
            with self.subTest():
                self.assertRaises(TypeError,BinTreeNode.insert,BinTreeNode,error,True)



    def test_search(self):
        self.assertEqual(BinTreeNode.search(self.node.right,2),None)
        self.assertEqual(self.node.search(5),self.node)
        for node in nodes_to_insert:
            self.node.insert(node)
        self.assertEqual(self.node.search(3),None)
        self.assertEqual(self.node.search(1), self.node.left)
        self.assertEqual(self.node.search(7), self.node.right)
        for error in error_raise_tests:
            with self.subTest():
                self.assertRaises(TypeError,BinTreeNode.search,BinTreeNode,error,True)



    def tearDown(self) -> None:
        self.logPoint()



    def logPoint(self):
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))
