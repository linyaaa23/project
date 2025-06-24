class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # 1. 插入节点（简单按值插入，或按需设计规则）
    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
            return
        # 这里简单实现按层遍历插入（也可按二叉搜索树规则）
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

    # 2. 前序遍历（递归）
    def preorder_traverse(self, node):
        if node:
            print(node.data, end=" ")
            self.preorder_traverse(node.left)
            self.preorder_traverse(node.right)

    # 3. 查找节点
    def search(self, data, node=None):
        node = node or self.root
        if not node:
            return False
        if node.data == data:
            return True
        return self.search(data, node.left) or self.search(data, node.right)