import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.append(BASE_DIR)
import unittest
from data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.ll.append(10)
        self.ll.append(20)
        self.ll.append(30)

    def test_append(self):
        self.ll.append(40)
        self.assertEqual(self.ll.search(40), True)

    def test_delete(self):
        self.ll.delete(20)
        self.assertEqual(self.ll.search(20), False)

    def test_traverse(self):
        # 简单验证输出（可优化为捕获打印内容断言）
        self.ll.traverse()

if __name__ == '__main__':
    unittest.main()