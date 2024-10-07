import time
from random import randint
from threading import Thread, Lock

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()
    def deposit(self):
        for j in range(100):
            rand = randint(50, 500)
            self.balance += rand
            print(f'Пополнение: {rand}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.0000001)
    def take(self):
        for j in range(100):
            rand_t = randint(50,500)
            print(f'Запрос на {rand_t}')
            if rand_t <= self.balance:
                self.balance -= rand_t
                print(f'Снятие: {rand_t}. Баланс: {self.balance}')
            if rand_t > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')