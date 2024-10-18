import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


file_names = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == "__main__":

    start = datetime.datetime.now()
    for file_name in file_names:
        read_info(file_name)
    end = datetime.datetime.now()
    print(f'{end - start} (Линейный)')

    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, file_names)
        end = datetime.datetime.now()
    print(f'{end - start} (Многопроцессорный)')
