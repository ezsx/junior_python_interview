import threading

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            new_balance = self.balance + amount
            self.balance = new_balance

    def withdraw(self, amount):
        with self.lock:
            new_balance = self.balance - amount
            self.balance = new_balance

def perform_transactions(account, transactions):
    for transaction in transactions:
        if transaction > 0:
            account.deposit(transaction)
        else:
            account.withdraw(abs(transaction))

# Create a bank account and some transactions
account = BankAccount(1000)
transactions = [100, -200, 300, -100, 50, -25]

# Create threads to perform transactions
import time
time1 = time.perf_counter()
for i in range(100):
    threads = [threading.Thread(target=perform_transactions, args=(account, transactions)) for _ in range(20)]

    # Start the threads
    for t in threads:
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print(f"Final account balance: {account.balance}")
print(time.perf_counter()-time1)
