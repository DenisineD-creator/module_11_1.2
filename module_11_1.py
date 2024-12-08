from time import time
from multiprocessing import Pool

def measure_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = round(seconds % 60, 6)
    return f'{hours:02}:{minutes:02}:{seconds:06}'

def read_info(name):
    all_data = []
    with open(name) as f:
        for line in f:
            all_data.append(line)


filenames = ['files\\file 1.txt', 'files\\file 2.txt', 'files\\file 3.txt', 'files\\file 4.txt']

if __name__ == '__main__':
    start = time()
    for filename in filenames:
        read_info(filename)

    end = time()
    print(measure_time(end - start), '(линейный)')

    start = time()
    with Pool(4) as p:
        p.map(read_info, filenames)
    end = time()
    print(measure_time(end - start), '(многопроцессный)')



