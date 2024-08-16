import numpy as np
from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")
ages_x=[25,26,27,28,29,30,31,32,33,34,35]
x_indices=np.arange(len(ages_x))
width=0.25

dev_y=[38000,40000,42000,44000,48000,53000,55000,56000,60000,62000,65000]
plt.bar(x_indices,dev_y,width=width,label="All Devs")
#to plot bar chart use bar instead of plot
py_dev_y=[45000,48000,51000,54000,60000,63000,66000,70000,73000,78000,80000]
plt.bar(x_indices+width,py_dev_y,width=width,label="Python")

plt.xticks(ticks=x_indices,labels=ages_x)
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Salary (Rupees) by Age")

plt.legend()
plt.show()