# coding: utf-8
MA = np.array([[1,2],[2,3]])
b = 6
b = np.array([1,2])
x = np.linalg.inv(MA)*MA/b*np.linalg.inv(MA)
x
A = np.array([[1,2],[3,4]])
b = np.array([1,2])
x = np.linalg.inv(A) * A
x
y = np.linalg.inv(A) * b
y
y = np.linalg.inv(A).dot(b)
y
A
x = np.linalg.inv(A).dot(b)
x
A
b
#inverse of metrix mutipled by a value
x = np.linalg.solve(A,b)
x
