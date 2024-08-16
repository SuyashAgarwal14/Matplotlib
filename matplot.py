from matplotlib import pyplot as plt
import numpy as np
fig=plt.figure()                                           #create a new figure

ax1=fig.add_subplot(2,2,1)                                 #add axes to figure as part of subplot arrangement
ax1.hist(np.random.standard_normal(100),bins=20,color="black",alpha=0.6)

ax2=fig.add_subplot(2,2,2)
ax2.scatter(np.arange(30),np.arange(30)+3*np.random.standard_normal(30))

ax3=fig.add_subplot(2,2,3)
ax3.plot(np.random.standard_normal(50).cumsum(),color="black", linestyle="dashed")


fig, axes= plt.subplots(2,2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.standard_normal(500), bins=50,color="black",alpha=0.5)
        
fig.subplots_adjust(wspace=1, hspace=0)                    #adjust spaces between subplots

plt.show()