#!/usr/bin/env python
# maze.py
from maze0 import Maze0
import random
try:
    from disjSets import DisjSets
except ImportError:
    from disjSets0 import DisjSets
from random import seed, randrange
class Maze(Maze0):
    def isGood(self):
        nICBs=self.m*(self.n-1)+self.n*(self.m-1)
        up=nICBs
        connect=DisjSets(nICBs) #connect the boundaries
        # if the wallUp is False, reduce the number of nCIBs. When the loop finishes,
        # the number of boundaries should be (m-1)*(n-1) and all connect(i) is equal
        for i in range(nICBs):
            if self.wallUp[i]==False:
                up=up-1
                connect.union(connect(self.side1[i]),connect(self.side2[i]))
        for i in range(nICBs):
            if connect(i)!=connect(i+1):
                return False
            else:
                if up==(self.m-1)*(self.n-1):
                    return True
    def makeGood(self):
        nICBs=self.m*(self.n-1)+self.n*(self.m-1)
        connect=DisjSets(nICBs)
        seed(a=2014)
        chosen=set()
        up=nICBs
        # choose random ICB, if they do not equal, connect them until every cell is connected
        while up>0:
            i=randrange(0,nICBs)
            if i not in chosen:
                if connect(self.side1[i])!=connect(self.side2[i]):
                    self.wallUp[i]=False
                    connect.union(connect(self.side1[i]),connect(self.side2[i]))
                set.add(chosen,i)
                up=up-1
        return True
if __name__=='__main__':
    mlist=[3,4,3]
    nlist=[3,3,4]
    downlist=[
        [1,3,4,5,6,8,10,11],
        [0,2,3,4,5,7,9,10,12,14,15,16],
        [0,2,3,5,8,11,13,14,15]]
    for k in range(3):
        m=mlist[k];n=nlist[k]; down=downlist[k]
        up=[True]*(m*(n-1)+n*(m-1))
        for d in down:
            up[d]=False
        maze=Maze(m,n,up=up)
        maze.print()
        print('maze.isGood()',maze.isGood())
        print()
    for k in range(2):
        maze=Maze(22,39)
        maze.makeGood()
        maze.print()
        print('maze.isGood()',maze.isGood())
        print()
        
                    
                
        
