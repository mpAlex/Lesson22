# Создайте класс Tomato
# Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# Создайте метод init(), внутри которого будут определены два динамических protected свойства:
# 1) _index - передается параметром и 2) _state - принимает первое значение из словаря states
# Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
class Tomato:
    states = {
              0: "Семечка",
              1: "Стебель",
              2: "Цветение",
              3: "Зеленый помидор",
              4: "Спелый помидор"
              }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 4:
            self._state += 1
        print(f'Томат {self._index} - {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 4:
            return True
        else:
            return False


# Создайте класс TomatoBush
# Определите метод init(), который будет принимать в качестве параметра количество томатов и на его основе будет создавать список объектов класса Tomato.
# Данный список будет храниться внутри динамического свойства tomatoes.
# Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая

class TomatoBush:
    def __init__(self, tomato_count):
        self.tomatoes = [Tomato(index) for index in range (tomato_count)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

# Создайте класс Gardener
# Создайте метод init(), внутри которого будут определены два динамических свойства:
# 1) name - передается параметром, является публичным и 2) _plant - принимает объект класса Tomato, является protected
# Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай. Если нет - метод печатает предупреждение.
# Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству.

class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print("Садовник работает")
        self._plant.grow_all()
        print("Работа завершена")

    def harvest(self):
        print("Садовник собирает урожай")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Сбор завершен")
        else:
            print("Томат еще не созревший")

    @staticmethod
    def knowledge_base():
        print("""Помидоры относятся к числу светолюбивых растений,
но при этом плохо переносят прямые солнечные лучи.
Идеальным местом для них считается грядка, притененная рядом расположенной теплицей или плодовым деревом.
Желательно, чтобы в этом районе не было сквозняков.""")

Gardener.knowledge_base()
tomato_bush = TomatoBush(5)
gardener = Gardener("Alex", tomato_bush)
tomato_bush.all_are_ripe()
gardener.work()
gardener.work()
gardener.harvest()
gardener.work()
gardener.work()
gardener.harvest()