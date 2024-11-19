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


linked_list = Linkedlist(34, 4)
linked_list.addFirst()
linked_list.addLast()
linked_list.deleteFirst()
