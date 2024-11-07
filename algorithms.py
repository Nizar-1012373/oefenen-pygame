class Array:
    def __init__(self, length, value):

        self.items = [value]
        self.length = length

    # def check_len(self):

    def length_of_array(self):
        new = self.items * self.length
        print(new)

    def print(self):
        i = 0

        for i in self.items:

            print(i)


array2 = Array(8, 0)


array2.length_of_array()
