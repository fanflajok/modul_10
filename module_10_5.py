import datetime
import multiprocessing


def read_info(name):
    all_data = []
    file = open(name, 'r', encoding='utf=8')
    for lines in (file.readlines()):
        all_data.append(lines.rstrip('\n'))


start = datetime.datetime.now()
for i in range(1,5):
    filenames = f'./file {i}.txt'
    read_info(filenames)
end = datetime.datetime.now()
print(end-start)
#0:00:02.346019


if __name__ == '__main__':
    with multiprocessing.Pool(processes=5) as pool:
        filenames = [f'./file {number}.txt' for number in range(1, 5)]
        start = datetime.datetime.now()
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)
#0:00:01.881725