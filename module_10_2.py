from threading import Thread
import time
class Knight(Thread):
    def __init__(self, name, power, nums_of_enemies = 100):
        super().__init__()
        self.name = str(name)
        self.power = int(power)
        self.nums_of_enemies = nums_of_enemies
    def run(self):
        print(f'{self.name}, на нас напали!')
        for i in range(self.nums_of_enemies):
            if self.nums_of_enemies < self.power:
                self.nums_of_enemies = self.power
            print(f'{self.name} сражается {i+1} дней(дня), осталось {self.nums_of_enemies - self.power} врагов')
            self.nums_of_enemies -= self.power
            time.sleep(1)
            if self.nums_of_enemies <= 0:
                print(f'{self.name} одержал победу спустя {i+1} дней(дня)!')
                return
first_knight = Knight('Link', 30)
second_knight = Knight('Young Link', 10)
third_knight = Knight('Wolf Link', 19)
fourth_knight = Knight('Twilight Link', 40)

first_knight.start()
second_knight.start()
third_knight.start()
fourth_knight.start()

first_knight.join()
second_knight.join()
third_knight.join()
fourth_knight.join()
print('Все битвы закончились!')



