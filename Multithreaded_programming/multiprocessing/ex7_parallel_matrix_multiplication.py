import multiprocessing
import random


def worker(a_row, b, result_queue):
    result = [sum(x * y for x, y in zip(a_row, b_col)) for b_col in zip(*b)]
    result_queue.put(result)


def parallel_matrix_multiplication(a, b):
    if len(a[0]) != len(b):
        raise ValueError("Matrix dimensions do not match for multiplication")

    result_queue = multiprocessing.Queue()
    processes = []

    for a_row in a:
        process = multiprocessing.Process(target=worker, args=(a_row, b, result_queue))
        processes.append(process)
        process.start()

    result = [result_queue.get() for _ in range(len(a))]

    for process in processes:
        process.join()

    return result


def random_matrix(rows, cols):
    return [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]


if __name__ == '__main__':
    a = random_matrix(3, 2)
    b = random_matrix(2, 4)

    print("Matrix A:")
    for row in a:
        print(row)

    print("\nMatrix B:")
    for row in b:
        print(row)

    result = parallel_matrix_multiplication(a, b)

    print("\nResult:")
    for row in result:
        print(row)
