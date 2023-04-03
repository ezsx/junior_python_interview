import multiprocessing

file_paths = [
    "file1.txt",
    "file2.txt",
    "file3.txt",
    "file4.txt",
    "file5.txt",
]

def process_file(file):
    with open(file, 'r') as f:
        num_lines = sum(1 for line in f)
    return num_lines

def main():
    pool = multiprocessing.Pool()
    count_numlines_in_files = pool.map(process_file, file_paths)
    pool.close()
    pool.join()
    print(count_numlines_in_files)