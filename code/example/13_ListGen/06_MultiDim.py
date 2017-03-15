#!/usr/bin/python3
'''
Multi-Dimensional List
'''
multiList =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print ('[col[1] for col in multiList]: ')
print ([col[1] for col in multiList])

print ('[multiList[i][i] for i in range(len(multiList))]: ')
print ([multiList[i][i] for i in range(len(multiList))])