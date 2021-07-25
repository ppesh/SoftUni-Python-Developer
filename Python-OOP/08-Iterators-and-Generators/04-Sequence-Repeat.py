class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number == 0:
            raise StopIteration
        if self.current_index == len(self.sequence):
            self.current_index = 0
        temp = self.sequence[self.current_index]
        self.current_index += 1
        self.number -= 1
        return temp


# Test Code
result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
