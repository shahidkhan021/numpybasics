import numpy as np

L = [1,2,3]

A = np.array([1,2,3])

for e in L:
    print(e)

print("+++++Array++++++")
for e in A:
    print(e)


L.append(4)
print(L)
#this code throw erro
# A.append(4)
