# k.povasin@innopolis.university
# идея решния была взята с лекции неделя 12 слайд 26
N = int(input())

class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 32  # степень двойки для bitmask
        self.mass = [None] * self.capacity  # [date, sum, set(checks)]

    def hash(self, key):
        parts = key.split('-')  # сохраняем результат
        temp = ''
        for p in parts:
            temp += p  # убрали '-'
        return int(temp) % self.capacity

    def doubleHash(self, key):
        parts = key.split('-')
        temp = ''
        for p in parts:
            temp += p
        # Теперь temp — строка, делаем из неё число для хеширования
        h = 0
        for i, b in enumerate(bytearray(temp, 'utf-8'), 1):
            h = h * 137 + b
        return 1 + (h % (self.capacity - 1))

    def resize(self):
        old = self.mass
        self.capacity *= 2
        self.mass = [None] * self.capacity
        self.size = 0
        for item in old:
            if item is not None:
                self.put_internal(item[0], item[1], item[2])

    def put_internal(self, date, cost, checks):
        h1 = self.hash(date)
        h2 = self.doubleHash(date)
        idx = h1

        while True:
            cell = self.mass[idx]
            if cell is None:
                self.mass[idx] = [date, cost, set(checks)]
                self.size += 1
                return
            if cell[0] == date:
                cell[1] += cost
                cell[2] |= checks
                return
            idx = (idx + h2) & (self.capacity - 1)

    def put(self, parts):
        date = parts[0]
        check = parts[2][1:]
        cost = float(parts[3][1:])

        h1 = self.hash(date)
        h2 = self.doubleHash(date)
        idx = h1

        while True:
            cell = self.mass[idx]
            if cell is None:
                self.mass[idx] = [date, cost, {check}]
                self.size += 1
                break
            if cell[0] == date:
                cell[1] += cost
                cell[2].add(check)
                break
            idx = (idx + h2) & (self.capacity - 1)

        if self.size * 1.33 > self.capacity:  # эмпирически лучше чем 0.75
            self.resize()

    def get(self):
        return self.mass


hm = HashMap()
import string
for _ in range(N):
    parts = input().split(maxsplit=4)
    hm.put(parts)

for item in hm.get():
    if item is not None:
        print(item[0], f"${item[1]:.2f}", len(item[2]))

# k.povasin@innopolis.university
import sys

input = sys.stdin.readline

# Хэш-таблица для строк (Custom_Key)
class KeyHashTable:
    def __init__(self, size=65536):
        self.size = size
        self.table = [None] * size

    def hash(self, s):
        h = 0
        p = 31
        for c in s:
            h = (h * p + ord(c)) % self.size
        return h

    def double_hash(self, s):
        h = 0
        for c in s:
            h = (h * 137 + ord(c)) % self.size
        return 1 + (h % (self.size - 1))

    def exists(self, s):
        idx = self.hash(s)
        step = self.double_hash(s)
        start = idx
        while True:
            cell = self.table[idx]
            if cell is None:
                return False
            if cell == s:
                return True
            idx = (idx + step) & (self.size - 1)
            if idx == start:
                return False

    def put(self, s):
        idx = self.hash(s)
        step = self.double_hash(s)
        while True:
            cell = self.table[idx]
            if cell is None:
                self.table[idx] = s
                return
            if cell == s:
                return
            idx = (idx + step) & (self.size - 1)


# ==================== Основное решение ====================

N = int(input())
last_time = [0] * 20001          # user_id <= 20000
used_keys = KeyHashTable()
served_users = [False] * 20001   # отмечаем успешных пользователей
served_count = 0

for _ in range(N):
    parts = input().split()
    user = int(parts[0])
    url = parts[1]
    key = parts[2]
    time = int(parts[3])

    # 1) проверка URL
    if not (url.startswith("http://") or url.startswith("https://")):
        print("No")
        continue

    # 2) проверка времени
    if last_time[user] and time - last_time[user] <= 6:
        print("No")
        continue

    # 3) проверка ключа
    if used_keys.exists(key):
        print("No")
        continue

    # Если прошли все проверки
    print("Yes")
    last_time[user] = time
    used_keys.put(key)
    if not served_users[user]:
        served_users[user] = True
        served_count += 1

print(served_count)
