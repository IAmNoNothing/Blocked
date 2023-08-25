def clamp(num, _min, _max):
    return min(max(num, _min), _max)


def lerp(x, y):
    return (x + y) / 2


def median(sequence):
    return sum(sequence) / len(sequence)
