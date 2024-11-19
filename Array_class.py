class Array:
    def __init__(self, length2):

        self.length2 = length2
        self.count = 0
        self.items = []

    def remove(self, index):
        item = 0

        for i in range(self.count - 1):
            if self.items[i] == self.items[index]:
                index += 1
                self.items[i] = self.items[i + 1]

        self.count -= 1
        return self.count

    def insert(self, item):
        self.count += 1
        for i in range(self.count):
            if self.check_if_string(item):

                self.items[: self.count]
                print(self.count)

                self.items.append(item)

                return self.items

    def check_if_string(self, item):
        if type(item) == str:

            return False
        if type(item) == int:
            return True

    def print(self):

        print(self.items, self.count)


array2 = Array(2)

array2.insert(93)
array2.insert(9)
array2.insert(5)
array2.insert(7)
array2.insert(54)
array2.insert(99)
array2.remove(0)

array2.print()
