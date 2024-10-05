import time
from time import sleep
import requests
from datetime import datetime
from threading import Thread
def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf=8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i+1} \n')
        time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_st = datetime.now()
write_words(10,'example1.txt')
write_words(30,'example2.txt')
write_words(200,'example3.txt')
write_words(100,'example4.txt')
time_e = datetime.now()
time_r = time_e - time_st
print(f'Работа потоков: {time_r}')

time_st2 = datetime.now()
thr_first = Thread(target = write_words, args=(10, 'example5.txt'))
thr_second = Thread(target = write_words, args=(30, 'example6.txt'))
thr_third = Thread(target = write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target = write_words, args=(100, 'example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()


thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()
time_e2 = datetime.now()
time_r2 = time_e2 - time_st2
print(f'Работа потоков: {time_r2}')

