import threading
from time import sleep
from random import randint

class Bank:

    list_of_moves = []

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            x = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance = self.balance + x
            Bank.list_of_moves.append(f'Пополнение: {x}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            y = randint(50, 500)
            if y <= self.balance:
                self.balance = self.balance - y
                Bank.list_of_moves.append(f'Снятие: {y}. Баланс: {self.balance}.')
                sleep(0.001)
            else:
                self.lock.acquire()
                print(f'Запрос на {y} отклонён, недостаточно средств. Баланс: {self.balance}')
                sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
for move in Bank.list_of_moves:
    print(move)
