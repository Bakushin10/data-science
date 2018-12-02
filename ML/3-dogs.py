import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_hight = 28 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_hight], stacked= True, color = ['b','r'])
plt.show()
