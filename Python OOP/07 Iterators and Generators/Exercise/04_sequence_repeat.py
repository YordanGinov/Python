class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index += 1
        if self.current_index < self.number:
            if self.current_index >= len(self.sequence):
                return self.sequence[self.current_index%len(self.sequence)]
            return self.sequence[self.current_index]
        raise StopIteration()


result = sequence_repeat('abc', 10)
for item in result:
    print(item, end='')
#
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end ='')
