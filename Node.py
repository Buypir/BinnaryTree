from student import Student


class Node:
    def __init__(self, data: Student, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def print(self):
        if self.left:
            self.left.print()
        print(self.data)
        if self.right:
            self.right.print()

    def insert(self, data: Student):
        if self.data is not None:
            if data.rating < self.data.rating:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data.rating > self.data.rating:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    @staticmethod
    def find_minimum(node):
        while node.left:
            node = node.left
        return node

    def delete(self, root, data: Student):
        parent = None
        current = root
        while current and current.data != data:
            parent = current
            if data.rating < current.data.rating:
                current = current.left
            else:
                current = current.right
        if current is None:
            return root
        if current.left is None and current.right is None:
            if current != root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                root = None
        elif current.left and current.right:
            heir = self.find_minimum(current.right)
            value = heir.data
            self.delete(root, heir.data)
            current.data = value
        else:
            if current.left:
                child = current.left
            else:
                child = current.right
            if current != root:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                root = child
        return root

    def find_node(self, group: str):
        if self.data.group == group:
            return self.data
        left_result = None
        right_result = None
        if self.left:
            left_result = self.left.find_node(group)
        if self.right:
            right_result = self.right.find_node(group)
        return left_result if left_result else right_result

    def delete_by_group(self, group: str):
        while True:
            node = self.find_node(group)
            if node is not None:
                self.delete(self, node)
            else:
                break

    def print_by_rating(self, rating: Student):
        if self.left:
            self.left.print_by_rating(rating)
        if self.data.rating > rating:
            print(self.data)
        if self.right:
            self.right.print_by_rating(rating)
