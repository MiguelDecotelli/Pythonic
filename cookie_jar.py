class Jar:
    def __init__(self, capacity=12, size=0):
        self.capacity = capacity
        self.size = size

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        self.size += n
        return self.size

    def withdraw(self, n):
        self.size -= n
        return self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Can't have negative capacity")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
        print(f"size: {self.size}")
        print(f"capacity: {self.capacity}")
        if self.size > self.capacity:
            raise ValueError("Cookie jar is full")
        elif self.size < 0:
            raise ValueError("Cookie jar is empty")

def main():
    jar = Jar(int(input("Set Jar's size: ")))
    jar.deposit(int(input("Cookies to store: ")))
    jar.withdraw(int(input("Cookies to take: ")))
    print(jar)

if __name__ == "__main__":
    main()
    