import numpy as np
import multiprocessing

def calculate_dot_product(row, matrix_b):
    return np.dot(row, matrix_b)

def parallel_dot_product(matrix_a, matrix_b):
    # Create a Pool object with the number of processes equal to the number of CPU cores
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        # Calculate the dot product of each row of matrix_a with matrix_b
        result = pool.starmap(calculate_dot_product, [(row, matrix_b) for row in matrix_a])

    return np.array(result)

def main():
    # Create two large matrices for demonstration
    matrix_a = np.random.randint(0, 1000, (1000, 1000))
    matrix_b = np.random.randint(0, 1000, (1000, 1000))

    # Run the parallel dot product calculation
    result = parallel_dot_product(matrix_a, matrix_b)

    # Print the result (optional)
    print(result)

if __name__ == '__main__':
    main()
