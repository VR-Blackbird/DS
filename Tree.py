from collections import deque


class Node:
    def __init__(self, parent, left=None, right=None, root=False) -> None:
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node--{self.parent}"

    def pre_order(self, node):
        yield node
        if node.left is not None:
            yield from self.pre_order(node.left)
        if node.right is not None:
            yield from self.pre_order(node.right)

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node)
        self.in_order(node.right)

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node)

    def level_order(self):
        container = deque()
        container.append(self)

        while container:
            element = container.popleft()
            yield element
            if element.left:
                container.append(element.left)
            if element.right:
                container.append(element.right)

    def get_children(self):
        print(self.childred)


child3 = Node(5)
child4 = Node(6)
child5 = Node(7)
child6 = Node(8)
child1 = Node(1, child3, child4)
child2 = Node(2, child5, child6)
root = Node(3, child1, child2)

root.in_order(root)
