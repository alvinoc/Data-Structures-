# creates a node and default data value is None
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# Implements LinkedList functionality
class LinkedList:
    def __init__(self):
        self.head = Node()

    # insert an element at the end of the list
    def append(self, data):
        newNode = Node(data)
        currNode = self.head
        while currNode.next is not None:
            currNode = currNode.next
        currNode.next = newNode

    # calculates the length of the list
    def length(self):
        total = 0
        currNode = self.head
        while currNode.next is not None:
            total += 1
            currNode = currNode.next
        return total

    # displays the list items
    def display(self):
        elements = []
        currNode = self.head
        while currNode.next is not None:
            currNode = currNode.next
            elements.append(currNode.data)
        print(elements)

    # return an element from specific index
    def get(self, index):
        if index >= self.length():
            print("ERROR: index out of range")
            return None
        currIndex = 0
        currNode = self.head
        while True:
            currNode = currNode.next
            if currIndex == index:
                return currNode.data
            currIndex += 1

    # Deletes an element from a specific index
    def erase(self, index):
        if index >= self.length():
            print("ERROR: index out of range")
            return
        currIndex = 0
        currNode = self.head
        while True:
            lastNode = currNode
            currNode = currNode.next
            if currIndex == index:
                lastNode.next = currNode.next
                return
            currIndex += 1

    # Insert an element at specific index
    def insert(self, index, data):
        if index>=self.length():
            print("ERROR: index out of range")
            return
        newNode = Node(data)
        currIndex = 0
        currNode = self.head
        while True:
            lastNode = currNode
            currNode = currNode.next
            if currIndex == index:
                lastNode.next = newNode
                newNode.next = currNode
                return
            currIndex += 1


# new instance of linked list
myList = LinkedList()

# appending elements in the list
myList.append(1)
myList.append(2)
myList.append(4)
myList.append(5)

myList.display()


print (myList.get(2))

myList.erase(2)

myList.display()
myList.insert(2, 10)
myList.display()