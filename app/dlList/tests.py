import unittest
from dlList import DoubleLinkedList


class TestEmpty(unittest.TestCase):
    def test_created(self):
        """
        Проверяет корректность состояния
        только что созданного пустого списка
        """
        linkedList = DoubleLinkedList()
        self.assertIsNone(linkedList .first())
        self.assertIsNone(linkedList .last())


class TestPush(unittest.TestCase):
    value = 12
    value2 = "123"

    def test_beginEndCompare(self):
        """
        Проверяет, что начало и конец списка
        после команды push() для пустого списка совпадают
        """
        linkedList = DoubleLinkedList()
        linkedList.push(self.value)
        self.assertEqual(linkedList .first(), linkedList.last())

    def test_beginEndDiff(self):
        """
        Проверяет, что начало и конец списка
        после команды push() для непустого списка не совпадают
        """
        linkedList = DoubleLinkedList()
        linkedList.push(self.value)
        linkedList.push(self.value2)
        self.assertNotEqual(linkedList .first(), linkedList.last())

    def test_value(self):
        """
        Проверяет, что после команды push()
        в конце списка оказывается правильно значение
        """
        linkedList = DoubleLinkedList()
        linkedList.push(self.value)
        self.assertEqual(linkedList .last().value, self.value)


class TestPop(unittest.TestCase):
    value = 12

    def test_empty(self):
        """
        Проверяет, что команда pop на пустом списке вызовет ислючение
        """
        linkedList = DoubleLinkedList()
        self.assertRaises(Exception, linkedList.pop)

    def test_emptyPop(self):
        """
        Проверяет корректность состояния списка,
        ставшего пустым после команды pop
        """
        linkedList = DoubleLinkedList()
        linkedList.push(1)
        linkedList.pop()
        self.assertIsNone(linkedList .first())
        self.assertIsNone(linkedList .last())
        self.assertEqual(linkedList .len(), 0)

    def test_value(self):
        """
        Проверяет, что команда pop возвращает значение,
        которое лежало в конце списка
        """
        linkedList = DoubleLinkedList()
        linkedList.push(self.value)
        item = linkedList.last().value
        self.assertEqual(linkedList .pop(), item)


class TestUnshift(unittest.TestCase):
    value = 12
    value2 = "123"

    def test_beginEndCompare(self):
        """
        Проверяет, что начало и конец списка
        после команды unshift() для пустого списка совпадают
        """
        linkedList = DoubleLinkedList()
        linkedList.unshift(self.value)
        self.assertEqual(linkedList .first(), linkedList.last())

    def test_beginEndDiff(self):
        """
        Проверяет, что начало и конец списка
        после команды unshift() для непустого списка не совпадают
        """
        linkedList = DoubleLinkedList()
        linkedList.unshift(self.value)
        linkedList.unshift(self.value2)
        self.assertNotEqual(linkedList .first(), linkedList.last())

    def test_value(self):
        """
        Проверяет, что после команды unshift()
        в конце списка оказывается правильно значение
        """
        linkedList = DoubleLinkedList()
        linkedList.unshift(self.value)
        self.assertEqual(linkedList .first().value, self.value)


class TestShift(unittest.TestCase):
    value = 12

    def test_empty(self):
        """
        Проверяет, что команда shift на пустом списке вызовет ислючение
        """
        linkedList = DoubleLinkedList()
        self.assertRaises(Exception, linkedList.shift)

    def test_emptyPop(self):
        """
        Проверяет корректность состояния списка,
        ставшего пустым после команды shift
        """
        linkedList = DoubleLinkedList()
        linkedList.unshift(1)
        linkedList.shift()
        self.assertIsNone(linkedList .first())
        self.assertIsNone(linkedList .last())
        self.assertEqual(linkedList .len(), 0)

    def test_value(self):
        """
        Проверяет, что команда shift возвращает значение,
        которое лежало в начале списка
        """
        linkedList = DoubleLinkedList()
        linkedList.unshift(self.value)
        item = linkedList.first().value
        self.assertEqual(linkedList .shift(), item)


class TestContains(unittest.TestCase):
    value = 34.2
    value2 = "value 'value'"

    def test_containsEmpty(self):
        """
        Проверяет, что на пустом листе вернёт false
        """
        linkedList = DoubleLinkedList()
        self.assertFalse(linkedList .contains(self.value))

    def test_containsAbset(self):
        """
        Проверяет, что при отсутсвтии элемента с таким значением
        вернёт false
        """
        linkedList = DoubleLinkedList()
        linkedList += self.value
        self.assertFalse(linkedList .contains(self.value2))

    def test_containsValue(self):
        """
        Проверяет, что при наличии элемента с таким значеинем вернёт true
        """
        linkedList = DoubleLinkedList()
        linkedList += self.value
        self.assertTrue(linkedList .contains(self.value))


class TestRemove(unittest.TestCase):
    value = 12
    value2 = "123"

    def test_removeEmpty(self):
        """
        Проверяет, что удаление элемента из пустого листа
        приводит к ошибке
        """
        linkedList = DoubleLinkedList()
        self.assertRaises(Exception, linkedList.remove, self.value)

    def test_removeAbset(self):
        """
        Проверяет, что удаление несуществующего элемента приводит к ошибке
        """
        linkedList = DoubleLinkedList()
        linkedList += self.value
        self.assertRaises(Exception, linkedList.remove, self.value2)

    def test_removeValue1(self):
        """
        Проверяет, что существующий элемент
        корректно удаляется из списка из 1 элемента
        """
        linkedList = DoubleLinkedList()
        linkedList += self.value
        linkedList.remove(self.value)
        self.assertFalse(linkedList .contains(self.value))

    def test_removeValue2(self):
        """
        Проверяет, что существующий элемент
        корректно удаляется из списка из нескольких элементов
        """
        linkedList = DoubleLinkedList()
        for i in range(10):
            linkedList += i
        linkedList += self.value
        for i in range(10):
            linkedList += i
        linkedList.remove(self.value)
        self.assertFalse(linkedList .contains(self.value))

    def test_removeValues(self):
        """
        Проверяет, что существующие одинаковые элементы
        корректно удаляются из списка
        """
        linkedList = DoubleLinkedList()
        for i in range(10):
            linkedList += i
        for i in range(10):
            linkedList += self.value
        for i in range(10):
            linkedList += i
        linkedList.remove(self.value)
        self.assertFalse(linkedList .contains(self.value))

    def test_removeDiffValues(self):
        """
        Проверяет, что существующие разные элементы
        корректно удаляются из списка
        """
        linkedList = DoubleLinkedList()
        for i in range(10):
            linkedList += i
        for i in range(10):
            linkedList += self.value
            linkedList += self.value2
        for i in range(10):
            linkedList += i
        linkedList.remove(self.value, self.value2)
        self.assertFalse(linkedList .contains(self.value))
        self.assertFalse(linkedList .contains(self.value2))


class TestLen(unittest.TestCase):
    _len = 10
    value = "someData"

    def test_len(self):
        linkedList = DoubleLinkedList()
        for i in range(self._len):
            linkedList += i
        self.assertEqual(len(linkedList), linkedList.len())
        self.assertEqual(linkedList .len(), self._len)

    def test_lenRemove(self):
        linkedList = DoubleLinkedList()
        for i in range(self._len):
            linkedList += i
        for i in range(self._len):
            linkedList += self.value
        len = linkedList.len()
        linkedList.remove(self.value)
        self.assertEqual(len, linkedList.len() + self._len)

    def test_lenPush(self):
        linkedList = DoubleLinkedList()
        for i in range(self._len):
            linkedList.push(i)
        self.assertEqual(linkedList .len(), self._len)

    def test_lenPop(self):
        linkedList = DoubleLinkedList()
        for i in range(self._len):
            linkedList.push(i)
        for i in range(self._len):
            linkedList.pop()
        self.assertEqual(linkedList .len(), 0)

    def test_lenUnshift(self):
        linkedList = DoubleLinkedList()
        for i in range(self._len):
            linkedList.unshift(i)
        self.assertEqual(linkedList .len(), self._len)

    def test_lenShift(self):
        linkedList = DoubleLinkedList()
        for i in range(self._len):
            linkedList.unshift(i)
        for i in range(self._len):
            linkedList.shift()
        self.assertEqual(linkedList .len(), 0)


if __name__ == "__main__":
    unittest.main()
