class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def get(self, index):
        if index < 0:
            return None

        current = self.head
        current_index = 0

        while current is not None:
            if current_index == index:
                print(current.data)
            current = current.next
            current_index += 1

        return None

    def remove(self, index):
        if index < 0:
            return

        if index == 0:
            if self.head is not None:
                self.head = self.head.next
            return

        current = self.head
        previous = None
        current_index = 0

        while current is not None:
            if current_index == index:
                if current.next is not None:
                    previous.next = current.next
                return
            previous = current
            current = current.next
            current_index += 1

    def insert(self, n, val):
        if n < 0:
            return

        new_node = Node(val)

        if n == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        current_index = 0

        while current is not None:
            if current_index == n - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            current_index += 1

    def print(self):
        current = self.head
        while current != None:
            print(current.data, end=" ")
            current = current.next
        print()


