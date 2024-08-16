import random
from matplotlib import pyplot as plt
import pandas as pd
from itertools import count
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_values=[]
y_values=[]

index=count()

def animate(i):
    x_values.append(next(index))
    y_values.append(random.randint(0,5))
#plotting multiple line stacking on top of each other instead of clearing out previous plot to solve clear axis
    plt.cla()
    plt.plot(x_values,y_values)

#used to run the animate function for particular interval(in milliseconds) and plot the values 
ani=FuncAnimation(plt.gcf(),animate,interval=1000,cache_frame_data=False)

plt.tight_layout()
plt.show()