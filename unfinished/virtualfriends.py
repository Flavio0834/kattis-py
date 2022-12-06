class UF:
    def __init__(self):
        self.people = []
        self.id = []
        self.size = []
        self.rang = []
        self.indexes = {}

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
                self.size[b] += self.size[a]
                if self.rang[b] == self.rang[a]:
                    self.rang[b] += 1
            else:
                self.id[b] = a
                self.size[a] += self.size[b]

    def connected(self, a, b):
        a = self.find(a)
        b = self.find(b)

        return a == b


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        F = int(input())

        tree = UF()

        for i in range(F):
            a, b = input().split()

            if a not in tree.people:
                tree.people.append(a)
                tree.indexes[a] = len(tree.id)
                tree.id.append(len(tree.id))
                tree.size.append(1)
                tree.rang.append(1)
            if b not in tree.people:
                tree.people.append(b)
                tree.indexes[b] = len(tree.id)
                tree.id.append(len(tree.id))
                tree.size.append(1)
                tree.rang.append(1)

            tree.union(tree.indexes[a], tree.indexes[b])

            print(tree.size[tree.find(tree.indexes[a])])
