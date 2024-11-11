class Array:
    def __init__(self, length, value, length2):

        self.length = length
        self.length2 = [length2]
        # self.items = [value] * self.removeAt()
        self.more_items = [value] * self.insert_in_array(0)

    def insert_in_array(self, value):
        self.length2[0] += 1

        return self.length2[value]

    def check_length_is_more(self):
        if self.insert_in_array(0):

            return self.more_items

    # def check_length_is_less(self):
    #     if self.removeAt():
    #         return self.items

    def print(self):
        for i in self.check_length_is_more():
            print(i)
        print(self.more_items)

    # def print_less(self):
    #     for i in self.check_length_is_less():
    #         print(f"less {i}")


array2 = Array(12, 1, 3)


# array2.print_less()
array2.print()
