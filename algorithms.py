class Array:
    def __init__(self, value, length2):

        self.length2 = [length2]
        # self.items = [value] * self.removeAt()
        self.more_items = [value] * self.insert_in_array(0)

    def insert_in_array(self, value):
        self.length2[1] += 1

        return self.length2[value]

    def print(self):
        for i in self.insert_in_array(1):
            i
        print(self.more_items)


array2 = Array(8, 1)


# array2.print_less()
array2.print()
# array2.print()
