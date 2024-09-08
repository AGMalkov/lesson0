from threading import Thread
from time import sleep

class Knight(Thread):

    def __init__(self, name=str, power=int):
        super().__init__()
        self.name = name
        self.power = power
        self.warriors = 100

    def run(self):

        print(f"{self.name}, на нас напали!")
        battle_time = 0

        while self.warriors > 0:
            battle_time += 1
            sleep(1)
            self.warriors -= self.power

            if self.warriors < 0:
                self.warriors = 0

            print(f"{self.name} сражается {battle_time} день(дня)..., осталось {self.warriors} воинов.")

        print(f'{self.name} одержал победу спустя {battle_time} дней(дня)!')

if __name__ == "__main__":
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()

    first_knight.join()
    second_knight.join()

    print("Все битвы закончились!")
