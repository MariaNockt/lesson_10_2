import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power, lock):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  # Общее количество врагов
        self.days = 0
        self.lock = lock

    def run(self):
        print(f"{self.name}, на нас напали!")

        while self.enemies > 0:
            time.sleep(1)  # Задержка в 1 секунду (1 день сражения)
            self.days += 1

            with self.lock:
                self.enemies -= self.power
                if self.enemies < 0:
                    self.enemies = 0

                print(f"{self.name}, сражается {self.days} день(дня)..., осталось {self.enemies} воинов.")

        with self.lock:
            print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание блокировки
lock = threading.Lock()

# Создание экземпляров класса
first_knight = Knight('Sir Lancelot', 10, lock)
second_knight = Knight("Sir Galahad", 20, lock)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание завершения сражений
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")