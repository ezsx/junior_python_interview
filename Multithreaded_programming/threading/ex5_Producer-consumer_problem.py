import threading
import queue
import random
import time


def producer(shared_queue, condition):
    while True:
        # Generate a random integer between 1 and 10
        integ = random.randint(1, 10)
        # Acquire the lock and append the integer to the shared queue
        with condition:
            shared_queue.put(integ)
            # Signal the consumer using the condition variable
            condition.notify()
        # Sleep for a short duration (e.g., 1 second)
        time.sleep(1)


def consumer(shared_queue, condition):
    while True:
        # Acquire the lock
        with condition:
            # Wait for the producer to signal using the condition variable
            condition.wait()
            # Remove an item from the shared queue and print it
            item = shared_queue.get()
            print(item)


# Create a shared queue and a condition variable
shared_queue = queue.Queue()
condition = threading.Condition()

# Create the producer and consumer threads
producer_thread = threading.Thread(target=producer, args=(shared_queue, condition))
consumer_thread = threading.Thread(target=consumer, args=(shared_queue, condition))

# Start the threads
producer_thread.start()
consumer_thread.start()

# Optionally, you can join the threads if you have a mechanism to stop them
