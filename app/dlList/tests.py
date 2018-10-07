import unittest
from dlList import DoubleLinkedList, Item

class TestEmpty(unittest.TestCase):
    def test_created(self):
        """Проверяет корректность состояния только что созданного пустого списка"""
        l = DoubleLinkedList()
        self.assertIsNone(l.first())
        self.assertIsNone(l.last())
        self.assertEqual(l.len(), 0)
        
class TestPush(unittest.TestCase):
    value = 12
    value2 = "123"
    def test_beginEndCompare(self):
        """Проверяет, что начало и конец списка после команды push() для пустого списка совпадают"""
        l = DoubleLinkedList()
        l.push(self.value)
        self.assertEqual(l.first(), l.last())
    def test_beginEndDiff(self):
        """Проверяет, что начало и конец списка после команды push() для непустого списка не совпадают"""
        l = DoubleLinkedList()
        l.push(self.value)
        l.push(self.value2)
        self.assertNotEqual(l.first(), l.last())
    def test_value(self):
        """Проверяет, что после команды push() в конце списка оказывается правильно значение"""
        l = DoubleLinkedList()
        l.push(self.value)
        self.assertEqual(l.last().value, self.value)

class TestPop(unittest.TestCase):
    value = 12
    def test_empty(self):
        """Проверяет, что команда pop на пустом списке вызовет ислючение"""
        l = DoubleLinkedList()
        self.assertRaises(Exception, l.pop)
    def test_emptyPop(self):
        """Проверяет корректность состояния списка, ставшего пустым после команды pop"""
        l = DoubleLinkedList()
        l.push(1)
        l.pop()
        self.assertIsNone(l.first())
        self.assertIsNone(l.last())
        self.assertEqual(l.len(), 0)
    def test_value(self):
        """Проверяет, что команда pop возвращает значение, которое лежало в конце списка"""
        l = DoubleLinkedList()
        l.push(self.value)
        item = l.last().value
        self.assertEqual(l.pop(), item)

class TestUnshift(unittest.TestCase):
    value = 12
    value2 = "123"
    def test_beginEndCompare(self):
        """Проверяет, что начало и конец списка после команды unshift() для пустого списка совпадают"""
        l = DoubleLinkedList()
        l.unshift(self.value)
        self.assertEqual(l.first(), l.last())
    def test_beginEndDiff(self):
        """Проверяет, что начало и конец списка после команды unshift() для непустого списка не совпадают"""
        l = DoubleLinkedList()
        l.unshift(self.value)
        l.unshift(self.value2)
        self.assertNotEqual(l.first(), l.last())
    def test_value(self):
        """Проверяет, что после команды unshift() в конце списка оказывается правильно значение"""
        l = DoubleLinkedList()
        l.unshift(self.value)
        self.assertEqual(l.first().value, self.value)

class TestShift(unittest.TestCase):
    value = 12
    def test_empty(self):
        """Проверяет, что команда shift на пустом списке вызовет ислючение"""
        l = DoubleLinkedList()
        self.assertRaises(Exception, l.shift)
    def test_emptyPop(self):
        """Проверяет корректность состояния списка, ставшего пустым после команды shift"""
        l = DoubleLinkedList()
        l.unshift(1)
        l.shift()
        self.assertIsNone(l.first())
        self.assertIsNone(l.last())
        self.assertEqual(l.len(), 0)
    def test_value(self):
        """Проверяет, что команда shift возвращает значение, которое лежало в начале списка"""
        l = DoubleLinkedList()
        l.unshift(self.value)
        item = l.first().value
        self.assertEqual(l.shift(), item)        
        
class TestContains(unittest.TestCase):
    value = 34.2
    value2 = "value 'value'"
    def test_containsEmpty(self):
        """Проверяет, что на пустом листе вернёт false"""
        l = DoubleLinkedList()
        self.assertFalse(l.contains(self.value))
    def test_containsAbset(self):
        """Проверяет, что при отсутсвтии элемента с таким значеинем вернёт false"""
        l = DoubleLinkedList()
        l += self.value
        self.assertFalse(l.contains(self.value2))
    def test_containsValue(self):
        """Проверяет, что при наличии элемента с таким значеинем вернёт true"""
        l = DoubleLinkedList()
        l += self.value
        self.assertTrue(l.contains(self.value))

class TestRemove(unittest.TestCase):
    value = 12
    value2 = "123"
    def test_removeEmpty(self):
        """Проверяет, что удаление элемента из пустого листа приводит к ошибке"""
        l = DoubleLinkedList()
        self.assertRaises(Exception, l.remove, self.value)
    def test_removeAbset(self):
        """Проверяет, что удаление несуществующего элемента приводит к ошибке"""
        l = DoubleLinkedList()
        l += self.value
        self.assertRaises(Exception, l.remove, self.value2)
    def test_removeValue1(self):
        """Проверяет, что существующий элемент корректно удаляется из списка из 1 элемента"""
        l = DoubleLinkedList()
        l += self.value
        l.remove(self.value)
        self.assertFalse(l.contains(self.value))
    def test_removeValue2(self):
        """Проверяет, что существующий элемент корректно удаляется из списка из нескольких элементов"""
        l = DoubleLinkedList()
        for i in range(10):
            l += i
        l += self.value
        for i in range(10):
            l += i
        old_len = l.len()
        l.remove(self.value)
        self.assertFalse(l.contains(self.value))
    def test_removeValues(self):
        """Проверяет, что существующие одинаковые элементы корректно удаляются из списка"""
        l = DoubleLinkedList()
        for i in range(10):
            l += i
        for i in range(10):
            l += self.value
        for i in range(10):
            l += i
        old_len = l.len()
        l.remove(self.value)
        self.assertFalse(l.contains(self.value))
    def test_removeDiffValues(self):
        """Проверяет, что существующие разные элементы корректно удаляются из списка"""
        l = DoubleLinkedList()
        for i in range(10):
            l += i
        for i in range(10):
            l += self.value
            l += self.value2
        for i in range(10):
            l += i
        old_len = l.len()
        l.remove(self.value, self.value2)
        self.assertFalse(l.contains(self.value))
        self.assertFalse(l.contains(self.value2))
        
class TestLen(unittest.TestCase):
    _len = 10
    value = "someData"
    def test_len(self):
        l = DoubleLinkedList()
        for i in range(self._len):
            l += i
        self.assertEqual(len(l), l.len())
        self.assertEqual(l.len(), self._len)
    def test_lenRemove(self):
        l = DoubleLinkedList()
        for i in range(self._len):
            l += i
        for i in range(self._len):
            l += self.value
        len = l.len()
        l.remove(self.value)
        self.assertEqual(len, l.len() + self._len)
    def test_lenPush(self):
        l = DoubleLinkedList()
        for i in range(self._len):
            l.push(i)
        self.assertEqual(l.len(), self._len)
    def test_lenPop(self):
        l = DoubleLinkedList()
        for i in range(self._len):
            l.push(i)
        for i in range(self._len):
            l.pop()
        self.assertEqual(l.len(), 0)
    def test_lenUnshift(self):
        l = DoubleLinkedList()
        for i in range(self._len):
            l.unshift(i)
        self.assertEqual(l.len(), self._len)
    def test_lenShift(self):
        l = DoubleLinkedList()
        for i in range(self._len):
            l.unshift(i)
        for i in range(self._len):
            l.shift()
        self.assertEqual(l.len(), 0)

if __name__ == "__main__":
    unittest.main()

