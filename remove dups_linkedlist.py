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

        current = self.head
        while current.next:
            current = current.next

        current.next = newNode


    def findDups(self):
        if not self.head:
            return

        current = self.head

        while current.next:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next
    
    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(20)
ll.append(20)
ll.append(30)

ll.findDups()
ll.printList()
