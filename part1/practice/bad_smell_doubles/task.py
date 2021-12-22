class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def asc_sorting(self):
        return sorted(self.lst, reverse=False)


sort = SomeClass()
print(sort.asc_sorting())



