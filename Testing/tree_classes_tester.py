import inspect
import unittest

from tree_classes import BinTree, BinTreeNode

node_list_options_to_be_inserted = [[3, 4, 6, 1, 5, 2, 7, 9, 11, 17, 12], [1, 4, 2, 6], [5, 5, 7, 6], [1, 1, 1, 1],[]]
node_output_verify = [[([3,7,1,4],[1,3,4,7])], [([5,4,3,2],[2,3,4,5])],[([],[])]]
#node_search_inputs = [([1,2,3,4],3,3),([5,2,1,19],3,None),([],3,None)]
class TestTreeFunctions(unittest.TestCase):

    """ Initialize trees, then insert lists of nodes into them using parametrization,
     then assert that these nodes exist in the tree, by returning
      the tree_returner_helper function."""
    def test_verify_insertion(self):
        self.logPoint()
        for list in node_list_options_to_be_inserted:
            tree = BinTree()
            for p in list:
                tree.insert(p)
                with self.subTest():
                    self.assertIn(p,BinTreeNode.tree_returner_helper(tree.root))


    """ Verify that the tree_returner_helper and get_tree functions are working
    as expected, by comparing the output of them (which is a list of the
     tree nodes sorted by value), with an actual value using parametrization. """

    def test_print_ordered(self):
        self.logPoint()
        for two_dimension_array in node_output_verify:
            tree = BinTree()
            for one_dimension_array, one_dimension_array_2 in two_dimension_array:
                for node in one_dimension_array:
                    tree.insert(node)
                with self.subTest():
                    self.assertEqual(one_dimension_array_2,BinTreeNode.tree_returner_helper(tree.root))


    """ Function that maps which test the program is currently executing. """
    def logPoint(self):
        current_test = self.id().split('.')[-1]
        calling_function = inspect.stack()[1][3]
        print('in %s - %s()' % (current_test, calling_function))

    """ def test_search_function(self):
           self.logPoint()
           for tree_insert_inputs,search_input,result in node_search_inputs:
               tree = BinTree()
               for value in tree_insert_inputs:
                   tree.insert(value)
               with self.subTest():
                   self.assertEqual(BinTreeNode.search(tree.root,search_input),result)"""