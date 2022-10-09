# Welcome to our Python playground!


# This DividerIterator class is an iterator that will start
# at a number `start` and divide that number by `factor`
# over and over again until it is smaller than or equal
# to `end`.
class DividerIterator:
    def __init__(self, start, factor, end):
        self.start = start
        self.factor = factor
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < self.end:
            raise StopIteration
        current = self.current
        self.current = current / self.factor
        return current


# Let's keep dividing 100 by 7 over and over again
# until 0.01.
count = 0
for n in DividerIterator(100, 7, 0.01):
    print(f"Divided {count} times: {n}")
    count += 1