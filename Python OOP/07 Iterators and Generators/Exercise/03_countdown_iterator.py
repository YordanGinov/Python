class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current_num = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_num -= 1
        if self.current_num >= 0:
            return self.current_num
        raise StopIteration()


iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")

