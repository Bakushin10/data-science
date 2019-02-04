import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ex1data.txt", header = None)
X = data.iloc[:,0] # read first column
y = data.iloc[:,1] # read second column
m = len(y)
print(data.head())

# graph the data
plt.scatter(X,y)
plt.xlabel("population of city in 10000s")
plt.ylabel('Profit in $10,000s')
plt.show()

X = X[:,np.newaxis] # np.newaxis adds one more layer of demension
y = y[:,np.newaxis]
theta = np.zeros([2,1])
print(theta)
alpha = 0.01
ones = np.ones((m,1))
X = np.hstack((ones, X)) # adding the intercept term