class Array:
    def __init__(self, length2):

        self.length2 = length2

        self.items = []

    def insert(self, item):
        for i in range(self.length2):
            if self.check_if_string(item):
                if len(self.items) > self.length2:
                    return False
                else:
                    self.items.append(item)

            return self.items

    def remove(self, index):

        for i in range(self.length2):

            self.items[index] = self.items[index + 1]
            self.length2 -= 1
        return self.length2

    def check_if_string(self, item):
        if type(item) == str:

            return False
        if type(item) == int:
            return True

    def print(self):

        print(self.items)


array2 = Array(4)

array2.insert(93)
array2.insert(9)
array2.insert(5)
array2.insert(7)
array2.insert(54)

array2.remove(0)

array2.print()
