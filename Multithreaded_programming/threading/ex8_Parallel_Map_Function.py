import threading


def parallel_map(func, iterable):
    # Create a list to store the results and a list to store the threads
    results = [None] * len(iterable)
    threads = []

    # Define a worker function that will be executed by each thread
    def worker(index, value):
        # Apply the function to the value and store the result in the results list
        value = func(value)
        results[index] = value
        pass

    # Iterate through the items of the iterable
    for index, value in enumerate(iterable):
        # Create a new thread with the worker function and the index and value as arguments
        thread = threading.Thread(target=worker, args=(index, value))
        # Add the thread to the threads list and start it
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Return the results list
    return results
