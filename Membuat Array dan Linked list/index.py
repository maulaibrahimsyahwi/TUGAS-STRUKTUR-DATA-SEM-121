# Sebelum mengerjakan lihat document di README.md

#  CONTOH SEDERHANA PROGRAM ARRAY 
class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def insert(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("index diluar dari range ")
        self.array[index] = value

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index diluar dari range ")
        return self.array[index]

    def display(self):
        print(self.array)

# Example usage
array = Array(5)
array.insert(0, 100)
array.insert(1, 250)
array.insert(2, 500)
array.display() 
 # Output yang diharapkan : [100, 250, 500, None, None]



#  CONTOH SEDERHANA PROGRAM LINKED LIST


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def get(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.value
            count += 1
            current = current.next
        raise IndexError("Index diluar dari range")

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

# Example usage
linked_list = LinkedList()
linked_list.insert(30)
linked_list.insert(50)
linked_list.insert(80)
linked_list.display()  

# Output yang diharapkan :30 50 80