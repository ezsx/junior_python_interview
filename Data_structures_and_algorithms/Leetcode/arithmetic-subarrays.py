

def is_arithmetic_sequence(seq):
    if len(seq) < 2:
        return False
    diff = seq[1] - seq[0]
    for i in range(1, len(seq)):
        if seq[i] - seq[i - 1] != diff:
            return False
    return True
nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
l = [0,1,6,4,8,7]
r = [4,4,9,7,9,10]

answers = []
for left, right in zip(l, r):
    subArr = nums[left:right+1]
    print(subArr)
    if is_arithmetic_sequence(sorted(subArr)):
        answers += [True]
    else:
        answers += [False]
print(answers)