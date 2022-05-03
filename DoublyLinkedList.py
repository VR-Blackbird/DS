class Node:
    def __init__(self, data, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return f"Node-{self.data}"


class Doubly:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert_begin(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            itr = self.head
            left = itr.prev
            right = itr
            self.head = Node(data, left, right)
            itr.prev = self.head
            self.tail = itr

    def insert_end(self, data):
        if self.head is None:
            self.insert_begin(data)
        else:
            itr = self.head
            while itr.next is not None:
                itr = itr.next

            self.tail = Node(data, itr)
            itr.next = self.tail

    def insert_between(self, data, pos=0):
        if pos == 0:
            self.insert_begin(data)
        else:
            itr = self.head
            for i in range(pos - 1):
                itr = itr.next
            left = itr
            right = itr.next
            n = Node(data, left, right)
            itr.next.prev = itr.next = n

    def print_list(self):
        itr = self.head
        while itr is not None:
            print(f"{itr.prev} -- {itr} -- {itr.next}")
            itr = itr.next


d = Doubly()
d.insert_end(10)
d.insert_begin(20)
d.insert_end(30)
print(d.head, d.tail)
d.insert_between(40, 2)
d.print_list()
