def sum_negative_between_min_max(arr):
    if len(arr) < 3:  # Если элементов меньше 3, между min и max не может быть элементов
        return 0

    # Находим индексы минимального и максимального элементов
    min_idx = arr.index(min(arr))
    max_idx = arr.index(max(arr))

    # Определяем границы диапазона (исключаем сами min и max)
    left = min(min_idx, max_idx) + 1
    right = max(min_idx, max_idx)

    # Суммируем отрицательные элементы в диапазоне
    sum_negative = sum(x for x in arr[left:right] if x < 0)

    return sum_negative

# Пример использования
A = [3, -5, 7, -2, 9, -8, 4, -1]
arr = [3, -5, 7, -2, 9, -8, 4, -1]
min_val = min(arr)          # -5
max_val = max(arr)          # 9
min_index = arr.index(-5)   # 1
max_index = arr.index(9)    # 4
left = min(1,4) + 1         # 2
right = max(1,4)            # 4
total = 0
for i in range(2, 4):       # i = 2, 3
    if arr[i] < 0:          # arr[2]=7 – нет, arr[3]=-2 – да
        total += arr[3]     # total = -2
print(total)                # -2
