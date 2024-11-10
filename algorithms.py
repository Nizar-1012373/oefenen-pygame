class Array:
    def __init__(self, length, value):

        self.length = length
        self.items = [value] * self.length

    def insert_in_array(self):
        self.length += 1

        return self.length

    def check_length_is_more(self):
        if self.insert_in_array():
            return self.items

    def print(self):
        for i in self.items:
            print(i)


array2 = Array(3, 0)

array2.check_bigger()
array2.print()
