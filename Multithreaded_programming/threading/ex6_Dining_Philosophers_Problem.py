import threading
import time
import random

def philosopher(philosopher_id, left_fork, right_fork):
    while True:
        # Philosopher thinks
        start_think=time.perf_counter()
        time.sleep(random.uniform(0.5, 1))
        print(f"philosopher number:{philosopher_id}")

        # Philosopher tries to pick up the left fork
        left_fork.acquire()

        # Check if the right fork is available
        success = right_fork.acquire(timeout=0.5)

        if success:
            # Philosopher eats
            time.sleep(random.uniform(0.5, 1))
            print(f"eats{time.perf_counter()-start_think}")

            # Release both forks
            right_fork.release()

        # Release the left fork
        left_fork.release()

num_philosophers = 5

# Create forks (represented by Lock objects)
forks = [threading.Lock() for _ in range(num_philosophers)]

# Create philosopher threads
philosophers = []
for i in range(num_philosophers):
    philosopher_thread = threading.Thread(
        target=philosopher,
        args=(i, forks[i], forks[(i + 1) % num_philosophers]),
    )
    philosophers.append(philosopher_thread)


# Start the philosopher threads
for p in philosophers:
    p.start()

# Join the philosopher threads (optional, if you have a mechanism to stop them)
for p in philosophers:
    p.join()
