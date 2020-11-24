

class UF:

    def __init__(self, n: int):

        self.n = []
        for i in range(n+1):
            self.n.append(i)

    def union(self, p: int, q: int):
        pid = self.n[p]
        qid = self.n[q]
        for i in range(len(self.n)):
            if self.n[i] == pid:
                self.n[i] = qid

    def connected(self, x: int, y: int):
        return x == y

    def no_components(self):
        for i in self.n:
            print(i)


def main_function():
    n = int(input("Enter total connections: "))
    union_find = UF(int(n))

    while n != 0:
        a = int(input("Enter connection 1: "))
        b = int(input("Enter connection 2: "))

        if not union_find.connected(a, b):
            union_find.union(a, b)
            print(str(a) + " and  " + str(b) + " have been united.")
        n -= 1

    print("Total components are: " + str(union_find.no_components()))


if __name__ == "__main__":
    main_function()


