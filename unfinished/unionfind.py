class UF:
    def __init__(self, n):
        self.id = [i for i in range(n)]

    def find(self, a):
        while self.id[a] != a:
            a = self.id[a]

        return a

    def union(self, a, b):
        if not self.connected(a, b):
            self.id[self.find(a)] = self.find(b)

    def connected(self, a, b):
        while self.id[a] != a or self.id[b] != b:
            a = self.id[a]
            b = self.id[b]

        return True if a == b else False


if __name__ == "__main__":
    N, Q = map(int, input().split())
    tree = UF(N)

    for i in range(Q):
        q, a, b = input().split()
        a = int(a)
        b = int(b)

        if q == "?":
            print("yes" if tree.connected(a, b) else "no")
        else:
            tree.union(a, b)
