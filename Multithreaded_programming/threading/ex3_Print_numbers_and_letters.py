def print_even_numbers():
    print([i for i in range(2, 22, 2)])

def print_odd_numbers():
    print([i for i in range(1, 21, 2)])

import threading

t1 = threading.Thread(target=print_even_numbers())
t2 = threading.Thread(target=print_odd_numbers())

# Start the threads
t1.start()
t2.start()


# Wait for both threads to finish
t1.join()
t2.join()

print("Done!")