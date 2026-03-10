class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def get_grandparent(self):
        if self.parent:
            return self.parent.parent
        return None

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        x = self
        y = x.left

        if y is None:
            return

        parent = x.parent

        x.left = y.right
        if y.right is not None:
            y.right.parent = x

        y.parent = parent
        if parent is not None:
            if parent.left == x:
                parent.left = y
            else:
                parent.right = y

        y.right = x
        x.parent = y

    def rotate_left(self):
        x = self
        y = x.right

        if y is None:
            return

        parent = x.parent

        # Move y's left subtree to x's right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x

        # Link y to x's parent
        y.parent = parent
        if parent is not None:
            if parent.left == x:
                parent.left = y
            else:
                parent.right = y

        # Put x under y
        y.left = x
        x.parent = y


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)


    def fix(self, node):
        while node.parent is not None and node.parent.is_red():
            parent = node.parent
            grand = node.get_grandparent()

            if parent == grand.left:
                uncle = grand.right

                if uncle is not None and uncle.is_red():
                    parent.make_black()
                    uncle.make_black()
                    grand.make_red()
                    node = grand
                else:
                    if node == parent.right:
                        node = parent
                        node.rotate_left()

                    parent.make_black()
                    grand.make_red()
                    grand.rotate_right()

            else:
                uncle = grand.left

                if uncle is not None and uncle.is_red():
                    parent.make_black()
                    uncle.make_black()
                    grand.make_red()
                    node = grand
                else:
                    if node == parent.left:
                        node = parent
                        node.rotate_right()

                    parent.make_black()
                    grand.make_red()
                    grand.rotate_left()

        while node.parent is not None:
            node = node.parent
        node.make_black()
        

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" + self.__str_helper(node.left) + " <- " + str(node) + "]"
        return (
            "["
            + self.__str_helper(node.left)
            + " <- "
            + str(node)
            + " -> "
            + self.__str_helper(node.right)
            + "]"
        )
