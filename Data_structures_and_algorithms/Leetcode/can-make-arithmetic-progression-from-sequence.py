

def is_arithmetic_sequence(seq):
    if len(seq) < 2:
        return False
    diff = seq[1] - seq[0]
    for i in range(1, len(seq)):
        if seq[i] - seq[i - 1] != diff:
            return False
    return True

arr = [3,5,1]
print(sorted(arr))
arr = sorted(arr)
print(is_arithmetic_sequence(arr))



