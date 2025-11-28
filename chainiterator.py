class ChainIterator:
    def __init__(self, *sequences: tuple[list, ...]):
        self.sequences = sequences
        self.idx = 0
        self.sequence_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.sequence_idx += 1
            return self.sequences[self.idx][self.sequence_idx - 1]
        except IndexError:
            self.idx += 1
            self.sequence_idx = 1

            if self.idx == len(self.sequences):
                raise StopIteration

            return self.sequences[self.idx][self.sequence_idx - 1]


iterator = ChainIterator([1, 2, 3], [4], [5])
for element in iterator:
    print(element)
    