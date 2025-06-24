import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.append(BASE_DIR)
import unittest
from data_structures.tree import BinaryTree

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bt = BinaryTree()
        self.bt.insert(10)
        self.bt.insert(20)
        self.bt.insert(30)

    def test_insert(self):
        self.bt.insert(40)
        self.assertEqual(self.bt.search(40), True)

    def test_preorder_traverse(self):
        # 简单验证遍历逻辑（可优化断言）
        self.bt.preorder_traverse(self.bt.root)

if __name__ == '__main__':
    unittest.main()