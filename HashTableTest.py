import unittest

from main import HashTable


class MyTestCase(unittest.TestCase):
    def test_something(self):
        hash_table = HashTable()

        hash_table.insert("apple", 1)
        hash_table.insert("apricot", 2)
        hash_table.insert("banana", 3)
        hash_table.insert("berry", 4)

        hash_table.display()

        print("Получение значения по ключу:", hash_table.get("apple"))

        hash_table.update("apple", 10)
        print("Обновление значения:", hash_table.get("apple"))

        hash_table.delete("berry")
        hash_table.display()

        self.assertEqual(hash_table.get("apple"), 10)  # add assertion here


if __name__ == '__main__':
    unittest.main()
