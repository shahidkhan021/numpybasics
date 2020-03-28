# coding: utf-8
A = np.array([[1,2],[3,4]])
Ainv = np.linalg.inv(A)
Ainv
Ainv.dot(A)
Ainv * A
#Invers of matrix dot matrix give identity matrix
np.linalg.det(A)
np.diag(A)
#dot product is same as inner product vector cross multiplication or cross is  outer
a = np.array([[6,5],[7,6]])
b = np.array([[7,6],[5,6]])
np.outer(a,b)
b = np.array([[7,6],[5,6]])
np.outer(a,b)
np.outer(b,a)
b = np.array([7,6])
a = np.array([5,4])
np.outer(a,b)
np.diag(a)
np.diag(a).sum()
np.trace(a)
np.trace(A)
X = np.random.randn(100,3)
X = np.conv(X)
cov = np.cov(X)
cov.shape
#to find a convariance of data matrix first transpose it
cov = np.cov(X.T)
conv
cov
cov.shape
covnp.linalg.eigh(cov)
np.linalg.eigh(cov)
get_ipython().run_line_magic('save', 'eigh_vaue_eigh_vectory 78 - 111')
