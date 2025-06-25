import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.append(BASE_DIR)
import unittest
from data_structures.tree import BinaryTree

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt = BinaryTree()
        self.bt.insert("ELECTRONICS")
        self.bt.insert("FURNITURE")
        self.bt.insert("CLOTHING")

    def test_insert(self):
        self.assertTrue(self.bt.search("FURNITURE"))

    def test_search(self):
        self.assertFalse(self.bt.search("BOOKS"))

    def test_get_all_categories(self):
        categories = self.bt.get_all_categories()
        self.assertIn("ELECTRONICS", categories)

if __name__ == '__main__':
    unittest.main()