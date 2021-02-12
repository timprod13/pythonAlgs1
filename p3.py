"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
import heapq


# from collections import Counter


# решение c помощью модуля heapq O(N log N)
def solve_heap(my_dict):
    return heapq.nlargest(3, my_dict, key=my_dict.get)


# оптимальное решение с помощью модуля collections, а именно collections.Counter O(N)
# def solve_counter(my_dict):
#    return dict(Counter(my_dict).most_common(3))


# решение c помощью функции sorted O(N log N)
def solve_sorted(my_dict):
    return sorted(my_dict, key=my_dict.get, reverse=True)[:3]


def solve_for(my_dict):
    top_comp = []  # O(1)
    for i in range(3):  # O(N)
        max_val = ['', 0]  # O(1)
        for key, value in enumerate(my_dict):  # O(N) enumerate используем как замену счётчика
            if max_val[1] < my_dict[value]:  # O(1)
                max_val = [value, my_dict[value]]  # O(1)
        top_comp.append(max_val)  # O(1)
        my_dict.pop(max_val[0])  # O(1)
    return top_comp  # O(1)


storage = {'Alpha': 500, 'Beta': 1000, 'Gamma': 750, 'Delta': 1500, 'Epsilon': 220,
           'Eta': 2000, 'Yotta': 3000, 'Lambda': 1850, 'Omicron': 1660, 'Omega': 78}

print(storage)
print(solve_heap(storage))
# print(solve_counter(storage))
print(solve_sorted(storage))
print(solve_for(storage))

# наиболее оптимальным является решение с sorted, так как имеет меньшую сложность в сравнении с перебором двумя
# циклами for
