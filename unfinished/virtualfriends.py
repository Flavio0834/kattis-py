class UF:
    def __init__(self):
        self.people = []
        self.id = []

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
    T = int(input())
    for t in range(T):
        F = int(input())

        tree = UF()

        for i in range(F):
            a, b = input().split()

            if a not in tree.people:
                tree.people.append(a)
                tree.id.append(len(tree.id))
            if b not in tree.people:
                tree.people.append(b)
                tree.id.append(len(tree.id))

            tree.union(tree.people.index(a), tree.people.index(b))

            res = 0
            for k in range(len(tree.people)):
                if tree.connected(tree.people.index(a), k):
                    res += 1

            print(res)
