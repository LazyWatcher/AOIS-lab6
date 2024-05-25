class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):

        key = key.lower()
        hashValue = ord(key[0]) - ord('a')
        return hashValue % self.size

    def insert(self, key, value):

        index = self._hash(key)
        print(f"Ключ '{key}' Индекс {index}")
        new_node = Node(key, value)

        if not self.table[index]:
            self.table[index] = new_node
        else:
            current = self.table[index]
            while current.next and current.key != key:
                current = current.next
            if current.key == key:
                current.value = value
            else:
                current.next = new_node

    def get(self, key):

        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def delete(self, key):

        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False

    def update(self, key, value):

        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                current.value = value
                return True
            current = current.next
        return False

    def display(self):

        for i, node in enumerate(self.table):
            print(f"Index {i}:", end=" ")
            current = node
            while current:
                print(f"({current.key}: {current.value})", end=" -> ")
                current = current.next
            print("None")


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
