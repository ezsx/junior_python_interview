import threading


def print_numbers():
    for i in range(1, 11):
        print(i)


def print_letters():
    for letter in 'abcdefghij':
        print(letter)


# Create threads for each function
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# Start the threads
t1.start()
t2.start()


# Wait for both threads to finish
t1.join()
t2.join()

print("Done!")
