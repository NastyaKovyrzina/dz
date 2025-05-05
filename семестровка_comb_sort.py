import random
import os
import time
import matplotlib.pyplot as plt
from collections import defaultdict
from pathlib import Path

# 1 и 3 пункты: реализация сортировки расчёской на питоне и измерение количества итераций

def comb(massiv):
    iterations = 0
    step = int(len(massiv)/1.247)
    swap = 1
    while step > 1 or swap > 0:
        swap = 0
        i = 0
        while i + step < len(massiv):
            iterations += 1
            if massiv[i] > massiv[i+step]:
                massiv[i], massiv[i+step] = massiv[i+step], massiv[i]
                swap += 1
            i = i + 1
        if step > 1:
            step = int(step / 1.247)
    return massiv, iterations

# 2 пункт: создаем наборы случайных данных


if not os.path.exists("test_data"):
    os.mkdir("test_data")
    for i in range(50):
        n = random.randint(100, 10_000)
        data = [random.randint(-1000, 1000) for _ in range(n)]
        path = Path("test_data")
        filename = f"{path}/data_{n}_set_{i+1}.txt"
        with open(filename, "w") as f:
            f.write("\n".join(map(str, data)))


# Собираем все файлы с тестовыми данными
data_files = os.listdir("test_data")

# Для хранения результатов по размерам
results = defaultdict(list)

# 3 пункт: измерение среднего времени работы алгоритма

def average_time(algorithm, data, repeats=10):
    all_time = 0.0
    for _ in range(repeats):
        start_time = time.time()
        algorithm(data)
        end_time = time.time()
        all_time += end_time - start_time
    return all_time / repeats


# Обрабатываем каждый файл с тестовыми данными
for filename in data_files:
    with open(f"test_data/{filename}", "r") as f:
        data = list(map(int, f.read().splitlines()))

    size = len(data)

    time_taken = average_time(lambda x: comb(x)[0], data.copy())

    _, iterations = comb(data.copy())

    results[size].append((time_taken, iterations))

sizes = []
avg_times = []
avg_iterations = []

for size in sorted(results.keys()):
    times = [x[0] for x in results[size]]
    iters = [x[1] for x in results[size]]

    sizes.append(size)
    avg_times.append(sum(times) / len(times))
    avg_iterations.append(sum(iters) / len(iters))

# Построение графиков
plt.figure(figsize=(14, 10))

plt.subplot(2, 1, 1)
plt.scatter(sizes, avg_times, color='blue', alpha=0.5)
plt.plot(sorted(sizes), [avg_times[sizes.index(x)] for x in sorted(sizes)], 'b-')
plt.title('Зависимость времени выполнения от размера массива')
plt.xlabel('Размер массива')
plt.ylabel('Время (секунды)')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.scatter(sizes, avg_iterations, color='red', alpha=0.5)
plt.plot(sorted(sizes), [avg_iterations[sizes.index(x)] for x in sorted(sizes)], 'r-')
plt.title('Зависимость количества итераций от размера массива')
plt.xlabel('Размер массива')
plt.ylabel('Количество итераций')
plt.grid(True)

plt.tight_layout()
plt.show()

print("\nАнализ сложности алгоритма Comb Sort:")
print("1. На графике времени видно, что зависимость близка к квадратичной (O(n²))")
print("2. Однако при оптимальном выборе шага сложность может приближаться к O(n log n)")
print("3. Количество итераций растет быстрее линейного, но медленнее квадратичного")
print("4. Реальная производительность зависит от начального состояния данных")

