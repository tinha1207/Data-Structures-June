class UnionFind:
    """
    Index of array represents the node and value represents the root node
    """

    def __init__(self, size):
        self.root = [i for i in range(size)]  # Initializing the nodes array

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        """
        Checks if two nodes have the same root.  If they don't it will iterate through from 0 -> y
        until it finds rootY and sets it to rootX.

        i.e:
        union(1,2)
        root:  [0,1,2,3,4]
        index: [0,1,2,3,4]

        rootX == 1
        rootY == 2
        Iterate through and set root[2] -> 1
        root:  [0,1,1,3,4]
        index: [0,1,2,3,4]
        """
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)


# Test Case
uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
