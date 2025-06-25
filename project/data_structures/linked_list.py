class Node:
    def __init__(self, data=None):
        self.data = data  # 存储货物数据（字典）
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, item_id):
        if not self.head:
            return
        if self.head.data['item_ID'] == item_id:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data['item_ID'] != item_id:
            current = current.next
        if current.next:
            current.next = current.next.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, item_id):
        current = self.head
        while current:
            if current.data['item_ID'] == item_id:
                return current.data
            current = current.next
        return None