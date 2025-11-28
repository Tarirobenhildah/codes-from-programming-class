def generate_combinations(sequence, k):
    length = len(sequence)
    indices = list(range(k))

    while True:
        yield tuple(sequence[i] for i in indices)

        for i in reversed(range(k)):
            if indices[i] != i + length - k:
                break
        else:
            return

        indices[i] += 1
        for j in range(i+1, k):
            indices[j] = indices[j-1] + 1