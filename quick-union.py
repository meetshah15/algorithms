class QuickUnion():
    def __init__(self, n: int):
        self.n = []
        for i in range(n+1):
            self.n.append(i)

    def root(self, i: int):
        while i != self.n[i]:
            self.n[i] = i
        re

