#!/usr/bin/env python
# disjSets.py
class DisjSets:
    # elements indexed 0, 1, ..., n_elts
    def __init__(self, n_elts):
        self.s = list(range(n_elts))
        for i in list(range(n_elts)):
            self.s[i]=-1
    def union(self, root1, root2):
        if self.s[root1]==self.s[root2]:
            self.s[root1]=self.s[root1]-1
            self.s[root2]=root1
        elif self.s[root1]>self.s[root2]:
            self.s[root1]=root2
        else:
            self.s[root2]=root1
    def __call__(self, elt):
        if self.s[elt]<0:
            return elt
        else:
            return self.__call__(self.s[elt])
if __name__ == '__main__':
    ds = DisjSets(10)
    ds.union(ds(1), ds(2))
    ds.union(ds(5), ds(9))
    ds.union(ds(4), ds(6))
    ds.union(ds(6), ds(8))
    ds.union(ds(2), ds(4))
    ds.union(ds(3), ds(5))
    for i in range(10):
        print(ds(i), end=' ')
    print()
