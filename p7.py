"""
Задание 7.
Задание на закрепление навыков работы с деком

В рассмотренном на уроке листинге есть один недостаток
Приведенный код способен "обработать" только строку без пробелов, например, 'топот'

Но могут быть и такие палиндромы, как 'молоко делили ледоколом'

Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)
"""


# так как хочется успеть - взял пример с урока и добавил немного условий
# остальные писал с нуля
class DequeClass:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return self.elements == []

    def add_to_front(self, elem):
        self.elements.append(elem)

    def add_to_rear(self, elem):
        self.elements.insert(0, elem)

    def remove_from_front(self):
        return self.elements.pop()

    def remove_from_rear(self):
        return self.elements.pop(0)

    def size(self):
        return len(self.elements)


def pal_checker(string):
    dc_object = DequeClass()

    for el in string:
        dc_object.add_to_rear(el)

    still_equal = True

    while still_equal:  # перенёс условие количества оставшихся элементов в цикл для корректной отработки
        first = dc_object.remove_from_front()
        while ' ' in first and dc_object.size() > 1:
            first = dc_object.remove_from_front()
        last = dc_object.remove_from_rear()
        while ' ' in last and dc_object.size() > 1:
            last = dc_object.remove_from_rear()
        print(first + ' ' + last)
        if dc_object.size() < 2:
            return still_equal
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("мо л о ко           де              ли ли л ед            ок        ол о        м"))
