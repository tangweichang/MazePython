#!/usr/bin/env python
class DisjSets:
    def __init__(self, n_elts):
        self.s=list(range(n_elts))
    def union(self, root1, root2):
        for elt in range(len(self.s)):
            if self.s[elt]==root2:
                self.s[elt]=root1
    def __call__(self,elt):
        return self.s[elt]
if __name__=='__main__':
    ds= DisjSets(10)
    ds.union(ds(1),ds(2))
    ds.union(ds(5),ds(9))
    ds.union(ds(4),ds(6))
    ds.union(ds(6),ds(8))
    ds.union(ds(2),ds(4))
    ds.union(ds(3),ds(5))
    for i in range(10):
        print(ds(i),end=' ')
    print()   
    
