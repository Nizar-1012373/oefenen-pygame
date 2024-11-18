class Array:
    def __init__(self, length2):

        self.length2 = length2
        self.count = 0
        self.items = []

    def remove(self, index):

        for i in range(self.length2):

            self.items[index] = self.items[index + 1]
            self.length2 -= 1
            return self.length2

    def insert(self, item):

        for i in range(self.length2):
            if self.check_if_string(item):
                self.count += 1
                self.items[: self.count]

                self.items.append(item)

                return self.items

    def check_if_string(self, item):
        if type(item) == str:

            return False
        if type(item) == int:
            return True

    def print(self):

        print(self.items, self.count)


array2 = Array(6)

array2.insert(93)
array2.insert(9)
array2.insert(5)
array2.insert(7)
array2.insert(54)
array2.insert(99)
array2.remove(1)

array2.print()
