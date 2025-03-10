# import [package name] as [abbreviated name]
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
Sample data
np.random.seed(613) # set seed
x = np.arange(50) # 0,1,...,49
y = np.random.randint(0,100,50) # 50 random integers with min = 0, max = 99
Scatterplot
fig,ax = plt.subplots(figsize=(5,3)) # figure size
ax.scatter(x,y)