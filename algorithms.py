class Array:
    def __init__(self, length2):

        self.length2 = length2

        self.items = []

    def insert(self, item):
        for i in range(self.length2):
            self.items += [item]

    def print(self):

        print(self.items)


array2 = Array(1)


array2.insert(9)
array2.insert(93)
array2.insert(93)
