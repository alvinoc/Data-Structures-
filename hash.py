class Node:
    def _init_(self, data):
        self.data = data
        self.nextNode = None

    def getData(self):
        return self.data
        
class List:
    def _init_(self):
        self.firstNode = None
        self.lastNode = None

    def _str_(self):
        if self.is_empty():
            return "[]"
        currentNode = self.firstNode
        string = ""
        while currentNode is not None:
            string += "[" + str(currentNode.getData()) if len(string) == 0 else ", " + str(currentNode.getData())
            currentNode = currentNode.nextNode
        string += "]"
        return string    

    def insert_end(self, data):
        newNode = Node(data)
        if self.is_empty():
            self.firstNode = newNode
            self.lastNode = newNode
        else:
            self.lastNode.nextNode = newNode
            self.lastNode = newNode

    def remove(self, data):
        if self.is_empty():
            return 0
        currentNode = self.firstNode
        while currentNode.nextNode != None:
            if currentNode.nextNode.getData() == data:
                break
            currentNode = currentNode.nextNode
        
        nextNode = currentNode.nextNode.nextNode
        currentNode.nextNode = None
        currentNode.nextNode = nextNode
        return 0
            
            
    def length(self):
        if self.is_empty():
            return 0
        i = 1
        currentNode = self.firstNode
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
            i += 1
        return i

    def last(self):
        if self.is_empty():
            return None
        currentNode = self.firstNode
        while currentNode.nextNode != None:
            currentNode = currentNode.nextNode
        return currentNode.getData()

    def first(self):
        if self.is_empty():
            return None
        return self.firstNode.getData()

    def is_empty(self):
        return self.firstNode is None

class HashTable:
    def _init_(self, m):
        self.m = m
        self.table = [0] * m

    def hash_div(self, s):
        hash = 0
        for i in range(len(s)):
            hash += ord(s[i])
        
        index = i % self.m
        return index

    def insert(self, s, data):
        index = self.hash_div(s)
        if self.table[index]:
            self.table[index].insert_end(data)
        else:
            self.table[index] = List()
            self.table[index].insert_end(data)
    
    def search(self, s):
        index = self.hash_div(s)
        if self.table[index] != 0:
            print(self.table[index])

    def delete(self, s):
        index = self.hash_div(s)
        del self.table[index]

a = HashTable(10)
a.insert("iago", "teste")
a.insert("filipe", "aaaaa")
a.search("iago")
a.delete("iago")
a.search("iago")
a.search("filipe")
a.delete("filipe")
a.search("filipe")