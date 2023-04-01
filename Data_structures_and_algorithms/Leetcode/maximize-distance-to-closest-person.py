seats = [0] + [1, 0, 0, 0, 1, 0, 1]
zeros_left = 0
for i in seats:
    if i == 1:
        break
    zeros_left += 1

zeros_right = 0
for i in seats[::-1]:
    if i == 1:
        break
    zeros_right += 1
print(seats, zeros_left, zeros_right)
seats = seats[zeros_left:]
print(seats)
if zeros_right != 0:
    seats = seats[:-zeros_right]


def longest_gap_with_units(binary_array):
    n = len(binary_array)
    left_unit = -1  # index of leftmost unit seen so far
    right_unit = -1  # index of rightmost unit seen so far
    longest_gap = 0

    for i in range(n):
        if binary_array[i] == 1:
            if left_unit == -1:
                left_unit = i
            right_unit = i
        else:
            if left_unit != -1 and right_unit != -1:
                gap = i - left_unit - 1
                if i == n - 1 or binary_array[i + 1] == 1:
                    gap += 1  # include the unit on the right side
                longest_gap = max(longest_gap, gap)

    return longest_gap

print(longest_gap_with_units(seats))
