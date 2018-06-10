import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


points = 10000
periods = 10
amp = 4
phase = np.pi/4

x = np.linespace(0,2*np.pi*periods,num=points)
y = amp*np.sin(x+phase)

chosen_idx = np.random.choice(points, size=100, replace=False)

data1 = pd.Series(y[chosen_idx], index=x[chosen_idx])
plot1 = plt.plot(data1)
