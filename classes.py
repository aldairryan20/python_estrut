class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0
    def setHead(self, head):
        self.head = head

    def insertAtBeginning(self, data):
        newNode = Node(data)
        if self.length == 0:
            self.setHead(newNode)
        else:
            head = self.head
            self.head = newNode
            newNode.next = head
        self.length += 1

    def printList(self):
        curr = self.head
        while curr is not None:
            print(curr.data)
            curr = curr.next
