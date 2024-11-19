class Linkedlist:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def addFirst(self):
        print("add first")

    def addLast(self):

        print("add last")

    def deleteFirst(self):
        print("delete first")

    def contains(self):
        print("contains")

    def indexOf(self):
        print("indexOf")


class Node:
    def __init__(self, node1: int, node2: int, node3: int, node4: int):
        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        self.node4 = node4


linked_list = Linkedlist(34, 4)
linked_list.addFirst()
linked_list.addLast()
linked_list.deleteFirst()
