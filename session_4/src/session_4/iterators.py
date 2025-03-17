class EvenIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Use enumerate-like behaviour to track index and value
        while self.index < len(self.numbers):
            num = self.numbers[self.index]
            self.index += 1
            if num % 2 == 0:
                return num
        raise StopIteration


# Using enumerate to show index-value pairs
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = EvenIterator(items)
for num in even:
    print(num)


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Tutorial snippet: Generate and print first 10 Fibonacci numbers
for num in fibonacci(10):
    print("Fibonacci number:", num)
