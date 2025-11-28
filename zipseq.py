class ZipSequences:
    def __init__(self, *sequences):
        self.sequences = sequences
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        first_length = len(self.sequences[0])
        if self.index < first_length:
            result = []
            for seq in self.sequences:
                result.append(seq[self.index])
            self.index += 1
            return result
        raise StopIteration