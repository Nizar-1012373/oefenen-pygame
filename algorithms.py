class Array:
    def __init__(self, length, value):

        self.length = length
        self.items = [value] * self.insert_in_array()

    def insert_in_array(self):
        self.length += 1

        return self.length

    def check_length_is_more(self):
        if self.insert_in_array():

            return self.items

    # def removeAt(self):

    def print(self):
        for i in self.check_length_is_more():
            print(i)


array2 = Array(5, 0)

array2.check_length_is_more()
array2.print()
