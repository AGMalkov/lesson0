import threading
from time import sleep
from random import randint
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            i = randint(50, 500)
            with self.lock:
                self.balance = self.balance + i
                print(f'Пополнение: {i}. Баланс: {self.balance}')
                if self.balance >= 500 and self.lock.locked():
                    self.lock.release()
            sleep(0.001)

    def take(self):
        for _ in range(100):
            i = randint(50, 500)
            print(f'Запрос на {i}')
            with self.lock:
                if i <= self.balance:
                    self.balance = self.balance - i
                    print(f'Снятие: {i}. Баланс: {self.balance}.')
                else:
                    print(f'Запрос отклонён, недостаточно средств')

            sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
