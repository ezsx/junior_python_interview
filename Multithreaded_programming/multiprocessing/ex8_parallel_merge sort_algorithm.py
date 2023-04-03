import multiprocessing
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


def merge_sort_process(result_queue, arr):
    result_queue.put(merge_sort(arr))


def parallel_merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    result_queue = multiprocessing.Queue()
    left_process = multiprocessing.Process(target=merge_sort_process, args=(result_queue, left))
    right_process = multiprocessing.Process(target=merge_sort_process, args=(result_queue, right))

    left_process.start()
    right_process.start()

    left_sorted = result_queue.get()
    right_sorted = result_queue.get()

    left_process.join()
    right_process.join()

    return merge(left_sorted, right_sorted)


if __name__ == '__main__':
    arr = [random.randint(1, 1000) for _ in range(10000)]

    print("Unsorted array:")
    print(arr)

    sorted_arr = parallel_merge_sort(arr)

    print("\nSorted array:")
    print(sorted_arr)
