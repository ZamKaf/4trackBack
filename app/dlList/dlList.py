class Item:
    """
    Элемент двусвязного списка
    """
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.next: Item = next
        self.prev: Item = prev

    @staticmethod
    def get_item(value):
        """
        Проверяет, является ли элемент объетом класса Item
        Если да - возвращает его же,
        иначе - формирует новый объект с данным значением
        """
        if value is None:
            return None
        elif type(value) is Item:
            return value
        else:
            return Item(value)


class DoubleLinkedList:
    """
    Двусвязный список.
    """
    def __init__(self, value: Item = None):
        item = Item.get_item(value)
        self.begin = item
        self.end = item
        self.count = 0 if value is None else 1

    def push(self, value):
        item = Item.get_item(value)
        if 0 == self.count:
            self.end = self.begin = item
        else:
            item.prev = self.end
            self.end.next = item
            self.end = item
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise Exception("no more elements")
        value = self.end.value
        if self.count == 1:
            self.begin = None
            self.end = None
        else:
            self.end.prev.next = None
            self.end = self.end.prev
        self.count -= 1
        return value

    def unshift(self, value):
        item = Item.get_item(value)
        if 0 == self.count:
            self.end = self.begin = item
        else:
            item.next = self.begin
            self.begin.prev = item
            self.begin = item
        self.count += 1

    def shift(self):
        if self.count == 0:
            raise Exception("no more elements")
        value = self.begin.value
        if self.count == 1:
            self.begin = None
            self.end = None
        else:
            self.begin.next.prev = None
            self.begin = self.begin.next
        self.count -= 1
        return value

    def remove(self, *values):
        """
        Удаляет все элементы с такими значениями из списка
        Если ни одного элемента с таким значением найдено небыло -
        бросает исключение
        """
        flag_removed = False
        for value in values:
            for item in self:
                if item.value == value:
                    # Учитываем пограничные случаи
                    if item.prev is None and item.next is None:
                        self.begin = None
                        self.end = None
                    elif item.prev is None:
                        self.begin.next.prev = None
                        self.begin = self.begin.next
                    elif item.next is None:
                        self.end.prev.next = None
                        self.end = self.end.prev
                    else:
                        item.next.prev = item.prev
                        item.prev.next = item.next
                    self.count -= 1
                    flag_removed = True
        if not flag_removed:
            raise Exception("No such element")

    def contains(self, value) -> bool:
        for item in self:
            if item.value == value:
                return True
        return False

    def first(self) -> Item:
        return self.begin

    def last(self) -> Item:
        return self.end

    def len(self):
        return self.count

    def __len__(self):
        return self.len()

    @property
    def begin(self) -> Item:
        return self._begin

    @begin.setter
    def begin(self, value):
        self._currentIteratorElem = value
        self._begin = value

    @property
    def end(self) -> Item:
        return self._end

    @end.setter
    def end(self, value):
        self._end = value

    @property
    def is_empty(self) -> bool:
        return self.count == 0

    def __next__(self) -> Item:
        if self._currentIteratorElem is None:
            self._currentIteratorElem = self.begin
            raise StopIteration()
        item = self._currentIteratorElem
        self._currentIteratorElem = self._currentIteratorElem.next
        return item

    def __iter__(self):
        return self

    def print(self):
        for item in self:
            print(item.value)

    def concat(self, otherList):
        """
        Конкатенция двух списков
        В результате списки соединяются в один,
        и обе ссылки указывают на этот список
        Список состорит из элементов базовых списков
        """
        if len(otherList) == 0:
            otherList.begin = self.begin
            otherList.end = self.end
            otherList.count = self.count
            return
        if self.count == 0:
            self.begin = otherList.begin
            self.end = otherList.end
            self.count = otherList.count
            return

        self.end.next = otherList.begin
        otherList.begin.prev = self.end
        otherList.begin = self.begin
        self.end = otherList.end
        self.count += otherList.count
        otherList.count = self.count

    def __add__(self, other):
        if type(other) is DoubleLinkedList:
            first = self.copy()
            second = other.copy()
            first.concat(second)
            return first
        else:
            self.push(other)
            return self

    def __radd__(self, other):
        if type(other) is DoubleLinkedList:
            first = self.copy(other)
            second = self.copy(self)
            first.concat(second)
            return first
        else:
            self.shift(other)
            return self

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        self.pop()
        return self

    def __isub__(self, other):
        return self - other

    def copy(self):
        result = DoubleLinkedList()
        for item in self:
            result += Item(item.value)
        return result


def main():
    list = DoubleLinkedList("wer")
    for i in range(17):
        list.push(Item(i))
    list.print()
    print(list.shift())
    list += list.copy()
    list.print()


if __name__ == "__main__":
    main()
