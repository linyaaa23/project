class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # 1. 新增节点（尾部插入）
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # 2. 删除节点（按 item_ID 删除）
    def delete(self, item_id):
        if not self.head:
            return
        # 头节点匹配
        if self.head.data['item_ID'] == item_id:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data['item_ID'] != item_id:
            current = current.next
        if current.next:
            current.next = current.next.next

    # 3. 遍历链表
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 4. 查找节点（按 item_ID 查找）
    def search(self, item_id):
        current = self.head
        while current:
            if current.data['item_ID'] == item_id:
                return current.data
            current = current.next
        return None