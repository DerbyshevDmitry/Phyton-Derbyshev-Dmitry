class DoubleElement:

    def __init__(self, *array):
       self.array = array
       self.index = 0

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index + 1 == len(self.array):
            ans = (self.array[self.index], None)
        elif self.index >= len(self.array):
            raise StopIteration
        else:
            ans = (self.array[self.index], self.array[self.index + 1])
        self.index += 2
        return ans


dL = DoubleElement(1, 2, 3, 4)
for pair in dL:
    print(pair)

print()

dL = DoubleElement(1,2,3,4,5)
for pair in dL:
    print(pair)
