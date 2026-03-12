class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def print(self):
        if not self.head:
            return
        current = self.head
        while current:
            print(current.data)
            current = current.next


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print()
