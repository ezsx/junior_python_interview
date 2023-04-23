def twoSum(self, numbers: list[int], target: int) -> list[int]:
    i, j = 0, len(numbers) - 1
    while True:
        if target > numbers[i] + numbers[j]:
            i += 1
        elif target < numbers[i] + numbers[j]:
            j -= 1
        else:
            return [i + 1, j + 1]  # you only get to this line once