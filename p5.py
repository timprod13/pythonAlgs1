"""
Задание 5.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс)
# 2) lst = [[], [], [], [],....]
"""
import heapq  # так как разобрался в предыдущем задании с данным модулем, решил его использовать


class StackClass(object):

    def __init__(self, capacity):  # при создании стека указываем лимит в одном стеке
        self.stacks = [[]]
        self.index = [0]
        heapq.heapify(self.index)
        self.capacity = capacity

    def push(self, val):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])  # создаём пустой стек для очередного элемента
        self.stacks[-1].append(val)

    def pop(self):
        if len(self.stacks) == 0:
            return -1   # если затёрли все стеки - возвращаем пользователю -1
        val = self.stacks[-1].pop()
        while len(self.stacks) >= 1 and len(self.stacks[-1]) == 0:
            self.stacks.pop()  # затираем пустой стек после выталкивания очередного элемента
        return val


print("Создадим стек с лимитом 3 и добавим 8 элементов")
y = StackClass(3)
y.push(1)
y.push(2)
y.push(3)
y.push(4)
y.push(5)
y.push(6)
y.push(7)
y.push(8)
print(y.stacks)
print("Вытолкнем 4 элемента")
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
print("Добавим ещё 5")
y.push(9)
print(y.stacks)
y.push(10)
print(y.stacks)
y.push(11)
print(y.stacks)
y.push(12)
print(y.stacks)
y.push(13)
print(y.stacks)
print("Вытолкнем 10 элементов")
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
y.pop()
print(y.stacks)
