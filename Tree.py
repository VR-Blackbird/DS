from collections import deque


class Node:
    def __init__(self, parent, left=None, right=None, root=False) -> None:
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node--{self.parent}"


def pre_order(node):
    print(node)
    if node.left is not None:
        pre_order(node.left)
    if node.right is not None:
        pre_order(node.right)


def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)


def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node)


def level_order(node):
    container = deque()
    container.append(node)
    while container:
        element = container.popleft()
        yield element
        if element.left:
            container.append(element.left)
        if element.right:
            container.append(element.right)


child3 = Node(5)
child4 = Node(6)
child5 = Node(7)
child6 = Node(8)
child1 = Node(1, child3, child4)
child2 = Node(2, child5, child6)
root = Node(3, child1, child2)

print("-" * 38)
print("InOrder Traversal of binary Tree\n")
in_order(root)
print("-" * 38)
print("Pre-order Traversal of a binary Tree\n")
pre_order(root)
print("-" * 38)
print("Post-order Traversal of a binary Tree\n")
post_order(root)
print("-" * 38)
