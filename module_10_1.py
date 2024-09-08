from time import sleep
import threading
from datetime import datetime

def wite_words(word_count, file_name):
    with open(file_name, 'w') as f:
        for i in range(1, word_count + 1):
            f.write(f'Какое-то слово № {i} \n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

if __name__ == "__main__":
    time_start = datetime.now()

    wite_words(10, "example1.txt")
    wite_words(30, "example2.txt")
    wite_words(200, "example3.txt")
    wite_words(100, "example4.txt")

    time_end = datetime.now()
    time_res = time_end - time_start
    print(f'Работа потоков: {time_res}')

    time_start = datetime.now()

    thread1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
    thread2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
    thread3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
    thread4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    time_end = datetime.now()
    time_res = time_end - time_start
    print(f'Работа потоков: {time_res}')
