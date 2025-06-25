class TreeNode:
    def __init__(self, data=None):
        self.data = data  # 存储类别名称
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = TreeNode(data)
                return
            elif not current.right:
                current.right = TreeNode(data)
                return
            else:
                queue.append(current.left)
                queue.append(current.right)

    def preorder_traverse(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder_traverse(node.left)
            self.preorder_traverse(node.right)

    def search(self, data, node=None):
        node = node or self.root
        if not node:
            return False
        if node.data == data:
            return True
        return self.search(data, node.left) or self.search(data, node.right)

    def get_all_categories(self):
        categories = []
        def traverse(node):
            if node:
                categories.append(node.data)
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)
        return categories