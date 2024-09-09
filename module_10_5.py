import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start = datetime.now()
    for filename in filenames:
        read_info(filename)
    end = datetime.now()
    print(f'{end - start} (линейный)')
#0:00:08.998129 (линейный)

    start = datetime.now()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'{end - start} (многопроцессный)')
#0:00:04.171873 (многопроцессный)
