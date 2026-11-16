import os
import time
from multiprocessing import Process


def process_one():
    print(f"Процесс 1 запущен. PID: {os.getpid()}")
    time.sleep(2)
    print("Процесс 1 завершил работу.")
    return "Результат процесса 1"


def process_two():
    print(f"Процесс 2 запущен. PID: {os.getpid()}")
    time.sleep(3)
    print("Процесс 2 завершил работу.")
    return "Результат процесса 2"


def process_three():
    print(f"Процесс 3 запущен. PID: {os.getpid()}")
    time.sleep(4)
    print("Процесс 3 завершил работу.")
    return "Результат процесса 3"


def process_four():
    print(f"Процесс 4 запущен. PID: {os.getpid()}")
    time.sleep(5)
    print("Процесс 4 завершил работу.")
    return "Результат процесса 4"


if __name__ == "__main__":
    print(f"Главный процесс запущен. PID: {os.getpid()}")

    p1 = Process(target=process_one)
    p2 = Process(target=process_two)
    p3 = Process(target=process_three)
    p4 = Process(target=process_four)

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    print(f"ID процесса 1: {p1.pid}")
    print(f"ID процесса 2: {p2.pid}")
    print(f"ID процесса 3: {p3.pid}")
    print(f"ID процесса 4: {p4.pid}")

    p1.join()
    p2.join()
    p3.join()
    p4.join()

    print("\nВсе процессы завершили работу.")
    print("Результат: процесс 1 выполнен.")
    print("Результат: процесс 2 выполнен.")
    print("Результат: процесс 3 выполнен.")
    print("Результат: процесс 4 выполнен.")
