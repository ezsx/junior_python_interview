import multiprocessing

def square(x):

    return x * x

def main():
    pool = multiprocessing.Pool()
    numbers = [1, 2, 3, 4, 5]
    squares = pool.map(square, numbers)
    pool.close()
    pool.join()
    print(squares)

if __name__ == '__main__':
    main()
