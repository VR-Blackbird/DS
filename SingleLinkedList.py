class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"Node - {self.data}"


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        itr = self.head
        if itr is None:
            self.insert_at_start(data)
            return
        while True:
            if itr.next is None:
                node = Node(data)
                itr.next = node
                break
            itr = itr.next

    def insert_inbetween(self, data, pos=0):
        if pos == 0:
            self.insert_at_start(data)
        else:
            itr = self.head
            for i in range(pos - 1):
                itr = itr.next

            next_item = itr.next
            itr.next = Node(data, next_item)

    def get_length(self):
        itr = self.head
        length = 0
        if itr is not None:
            while itr is not None:
                length += 1
                itr = itr.next
        return length

    def remove_at_begin(self, edge="b"):
        itr = self.head
        if itr is None:
            raise Exception("No elements to remove")
        elif itr.next is not None:
            if edge == "b":
                self.head = itr.next
            else:
                length = self.get_length()
                i = 0
                while i < length - 2:
                    itr = itr.next
                    i += 1
                itr.next = None
        else:
            self.head = None

    def print_list(self):
        if self.head is None:
            return "Linked List is empty"
        itr = self.head
        while itr:
            print(itr)
            itr = itr.next


ll = LinkedList()

ll.insert_at_end(20)
ll.insert_at_end(21)
ll.insert_at_end(80)
ll.insert_inbetween(10, 2)
ll.insert_at_end(90)
ll.insert_at_end(900)
print(ll.get_length())
ll.remove_at_begin("e")
print(ll.print_list())
