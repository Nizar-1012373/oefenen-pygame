class Array:
    def __init__(self, length2):

        self.length2 = length2

        self.items = []

    def insert(self, item):
        for i in range(self.length2):
            if self.check_if_string(item):

                self.items += [item]

        return self.items

    def remove(self, index):
        if index > len(self.items):
            return self.items[index]

    def check_if_string(self, item):
        if type(item) == str:
            return False
        if type(item) == int:
            return True

    def print(self):

        print(self.items)


array2 = Array(1)

array2.insert(93)
array2.insert(9)
array2.insert(5)
array2.remove(2)

array2.print()
