class dictionary_iter:
    def __init__(self, dict_object):
        self.dict_object = dict_object
        self.keys = list(self.dict_object)
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index == len(self.dict_object):
            raise StopIteration
        key = self.keys[self.current_index]
        value = self.dict_object[key]
        self.current_index += 1
        return key, value


# Test Code
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


