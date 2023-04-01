from concurrent.futures import ThreadPoolExecutor, as_completed


def square(x):
    return x * x


numbers = [1, 2, 3, 4, 5]
results = []

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {executor.submit(square, n): n for n in numbers}

    for future in as_completed(futures):
        result = future.result()
        results.append(result)

print(results)
