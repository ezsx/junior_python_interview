import multiprocessing
import math


def factorial(number, result_dict):
    result = math.factorial(number)
    result_dict[number] = result

def main():
    # List of numbers for which we want to calculate factorials
    numbers = [5, 10, 15, 20]

    # Create a Manager object to manage a shared dictionary
    manager = multiprocessing.Manager()
    result_dict = manager.dict()

    # Create a list to store Process objects
    processes = []

    # Iterate through the list of numbers and create a Process for each
    for number in numbers:
        process = multiprocessing.Process(target=factorial, args=(number, result_dict))
        process.start()
        processes.append(process)

    # Wait for all processes to finish
    for process in processes:
        process.join()

    # Print the results
    for number, result in result_dict.items():
        print(f"Factorial of {number}: {result}")

if __name__ == '__main__':
    main()
