def hasNonNumberElements(data):
    for i in range(len(data)):
        if not isinstance(data[i], (int, float)):
            return True
    return False


def throwOnInvalidData(data):
    if hasNonNumberElements(data):
        raise TypeError("The data contains invalid elements")

def quickSort(data):
    throwOnInvalidData(data)
    if len(data) < 2:
        return data
    pivot = data[0]
    less = [i for i in data[1:] if i <= pivot]
    more = [i for i in data[1:] if i > pivot]
    return quickSort(less) + [pivot] + quickSort(more)