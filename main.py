import numpy as np

def remove_duplicates(lst):
    counts = {}
    for item in lst:
        counts[item] = counts.get(item, 0) + 1

    return [item for item in lst if counts[item] == 1]
def divide_polynoms(x, y):
    current_max_x_pow, max_y_pow = np.max(x), np.max(y)
    result, ostacha = np.array([]), np.array([])
    new_x = np.array([])
    while current_max_x_pow >= max_y_pow:
        current_max_x_pow = np.max(x)
        result = np.append(result, (current_max_x_pow - max_y_pow))
        temp_x = y + (current_max_x_pow - max_y_pow)
        new_x = np.array(remove_duplicates(np.append(x, temp_x)))
        x = new_x
        current_max_x_pow = np.max(x)

    ostacha = new_x
    return result, ostacha

def print_result(lst):
    x = [f"x^{int(i)}" for i in sorted(lst[0])]
    chastka = " + ".join(x).replace("x^1", "x").replace("x^0", "1")
    y = [f"x^{int(i)}" for i in sorted(lst[1])]
    ostacha = " + ".join(y).replace("x^1", "x").replace("x^0", "1")

    print("Результат\nЧастка: " + chastka + "\nОстача: " + ostacha)

# поліноми задаються у форматі масивів
# параметр 2 - масив степенів іксів діленого
# параметр 1 - масив степенів іксів дільника

x = np.array([4, 3, 2, 0])
y = np.array([3, 2])

try:
    print_result(divide_polynoms(x, y))
except Exception as e:
    print("Остача: 0")
