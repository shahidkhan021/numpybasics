# coding: utf-8
A = np.array([[1,1],[1.5,4]])
A
b = np.array([2200,5050])
b
x = np.linalg.solve(a,b)
b = np.array([2200,0],[5050,0])
b = np.array([[2200,0],[5050,0]])
x = np.linalg.solve(a,b)
x = np.linalg.solve(A,b)
x
b = np.array([2200,5050])
x = np.linalg.solve(A,b)
x
get_ipython().run_line_magic('save', 'word_proble 135-148')
