import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
sys.path.append(BASE_DIR)
import unittest
from data_structures.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()
        self.item1 = {'item_ID': 1, 'name': 'Laptop'}
        self.item2 = {'item_ID': 2, 'name': 'Mouse'}
        self.ll.append(self.item1)
        self.ll.append(self.item2)

    def test_append(self):
        self.assertEqual(self.ll.search(1), self.item1)

    def test_delete(self):
        self.ll.delete(1)
        self.assertEqual(self.ll.search(1), None)

    def test_search(self):
        self.assertEqual(self.ll.search(2)['name'], 'Mouse')

if __name__ == '__main__':
    unittest.main()