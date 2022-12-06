import sys


class UF:
    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.rang = [1 for i in range(n)]

    def find(self, a):
        while self.id[a] != a:
            a = self.id[a]

        return a

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if not self.connected(a, b):
            if self.rang[b] >= self.rang[a]:
                self.id[a] = b
                if self.rang[b] == self.rang[a]:
                    self.rang[b] += 1
            else:
                self.id[b] = a

    def connected(self, a, b):
        a = self.find(a)
        b = self.find(b)

        return True if a == b else False


if __name__ == "__main__":
    A = sys.stdin.readlines()
    N, Q = map(int, A[0].split())
    tree = UF(N)

    for i in range(1, Q + 1):
        q, a, b = A[i].split()
        a = int(a)
        b = int(b)

        if q == "?":
            print("yes" if tree.connected(a, b) else "no")
        else:
            tree.union(a, b)
