class Array:
    def __init__(self, length, value):

        self.items = [value] * length
        self.length = length

    def print(self):
        for i in self.items:
            print(i)


array2 = Array(8, 0)


array2.print()
