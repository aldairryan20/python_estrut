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
class Stack:
    def __init__(self, Capacity = 1):
        self.top = 1
        self.Capacity = Capacity
        self.A = [None]*Capacity   

    def push(self, data):
        if self.Capacity == self.top+1:
            print("Stack Overflow")
            return
        self.top+=1
        self.A[self.top] = data

    def pop(self):
        if self.top == -1:
            print ("Stack Underflow")
            return
        temp = self.A[self.top]
        self.A[self.top]-=1
        return temp

    def peek(self):
        if self.top==-1:
            print("Stack Underflow")
            return
        return self.A[self.top]
    
    def isEmpty(self):
        if self.length == 0: return True
        else: return False
    
    def Empty(self):
        for i in range(self.length):
            self.pop()