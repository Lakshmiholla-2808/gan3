class Pages:
    def __init__(self, total, size):
        self.total, self.size, self.start = total, size, 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.start >= self.total:
            raise StopIteration
        page = (self.start, min(self.start + self.size, self.total))
        self.start += self.size
        return page

for p in Pages(25, 10):
    print(p)
