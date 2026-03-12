class Node:
    def __init__(self):
        self.children = []


class XC3:
    def __init__(self, degree):
        self.root = self.build_tree(degree)
        self.degree = degree

    def build_tree(self, degree):
        node = Node()

        for k in range(1, degree + 1):
            if k <= 2:
                child_degree = 0
            else:
                child_degree = k - 2

            node.children.append(self.build_tree(child_degree))

        return node

    def height(self):
        def h(node):
            if not node.children:
                return 0
            return 1 + max(h(child) for child in node.children)

        return h(self.root)

    def num_nodes(self):
        def count(node):
            total = 1
            for child in node.children:
                total += count(child)
            return total

        return count(self.root)