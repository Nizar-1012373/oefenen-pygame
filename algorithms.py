class Array:
    def __init__(self, items, length2):

        self.length2 = length2

        self.items = items

    def insert(self, item):

        for i in range(self.length2):

            self.items += [item]
        print(self.items)


array2 = Array([], 1)


array2.insert(6)
array2.insert(2)
array2.insert(7)
