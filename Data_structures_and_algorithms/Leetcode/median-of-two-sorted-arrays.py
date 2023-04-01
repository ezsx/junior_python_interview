arr1 = [1, 2]
arr2 = [3]
arr_merged = []


def merge_sorted_arrays(arr1, arr2):
    i = 0
    j = 0
    m = len(arr1)
    n = len(arr2)
    merged_arr = []

    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    while i < m:
        merged_arr.append(arr1[i])
        i += 1

    while j < n:
        merged_arr.append(arr2[j])
        j += 1

    if len(merged_arr) % 2 == 0:
        median = (merged_arr[len(merged_arr) // 2] + merged_arr[len(merged_arr) // 2 - 1]) / 2
    else:
        median = merged_arr[len(merged_arr) // 2]

    return median


arr3 = merge_sorted_arrays(arr1, arr2)

print(arr3)
