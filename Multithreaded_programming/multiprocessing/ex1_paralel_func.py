import multiprocessing

def square(x):
    return x * x

def main():
    number = 4
    p = multiprocessing.Process(target=square, args=(number,))
    p.start()
    p.join()

if __name__ == '__main__':
    main()
