class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return

        current = self.root

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = BSTNode(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = BSTNode(value)
                    return
                current = current.right

    def search(self, value):
        current = self.root

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    def height(self):
        if self.root is None:
            return -1
        stack = [(self.root, 0)]
        max_h = 0
        while stack:
            node, depth = stack.pop()
            if depth > max_h:
                max_h = depth
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return max_h
