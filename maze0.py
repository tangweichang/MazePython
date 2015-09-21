#!/usr/bin/env python  
class Maze0:
    def __init__(self, m, n, up=True):
        nICBs = m*(n-1) + n*(m-1)  # ICB = Internal Cell Boundary
        side1 = [None]*nICBs; side2 =[None]*nICBs
        if up == True:
            wallUp = [True]*nICBs
        else:
            wallUp = up.copy()
        k = 0  # cell counter
        l = 0  # ICB counter
        for i in range(m):
            for j in range(n):
                if i < m - 1:  # there is a cell below
                    side1[l] = k; side2[l] = k + n; l += 1
                if j < n - 1:  # there is a cell to the right
                    side1[l] = k; side2[l] = k + 1; l += 1
                k += 1
        self.m = m; self.n = n
        self.side1 = side1; self.side2 = side2; self.wallUp = wallUp
    def print(self):
        m = self.m; n = self.n
        wallUp = self.wallUp
        l = 0  # ICB counter
        print('  '+' _'*(n-1))
        for i in range(m-1):
            print('|' if i > 0 else ' ', end='')
            for j in range(n-1):
                print('_' if wallUp[l] else ' ', end='')
                l += 1
                print('|' if wallUp[l] else ' ', end='')
                l += 1
            print('_|' if wallUp[l] else ' |')
            l += 1
        print('|', end='')
        for j in range(n-1):
            print('_|' if wallUp[l] else '_ ', end='')
            l +=1
        print()
