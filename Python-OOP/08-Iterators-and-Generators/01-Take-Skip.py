class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.current = 0
        self.iter = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iter <= self.count:
            count_num = self.current
            self.current += self.step
            self.iter += 1
            return count_num
        raise StopIteration()


# Test Code
numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
